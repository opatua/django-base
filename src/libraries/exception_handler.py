import logging
from logging import Logger
from typing import Dict, List, Optional

from django.core.exceptions import PermissionDenied
from django.http import Http404, JsonResponse
from rest_framework import exceptions, views
from rest_framework.exceptions import ErrorDetail


def exception_handler(exception, context=None):
    log_exception(exception, logging.getLogger(__name__))

    exception = to_api_exception(exception)

    errors = []
    if isinstance(exception.detail, dict):
        for key, error_details in exception.detail.items():
            errors.extend(_to_json_api_errors(error_details, key))
    else:
        errors.extend(_to_json_api_errors(exception.detail, None))

    views.set_rollback()

    response = JsonResponse(
        {
            # TODO Remove this once all clients stop parsing status from
            # response body
            "status": exception.status_code,
            "errors": errors,
        },
        status=exception.status_code,
    )

    if getattr(exception, "auth_header", None):
        response["WWW-Authenticate"] = exception.auth_header

    if getattr(exception, "wait", None):
        response["Retry-After"] = "%d" % exception.wait

    return response


def _to_json_api_error(error_detail, key: Optional[str]) -> Dict:
    error = {
        "detail": error_detail,
    }

    if key:
        error["source"] = {
            "pointer": key,
        }

    if isinstance(error_detail, ErrorDetail):
        error["code"] = error_detail.code

    return error


def _to_json_api_errors(error_details, key: Optional[str]) -> List:
    if not isinstance(error_details, list):
        error_details = [error_details]

    return [_to_json_api_error(error_detail, key) for error_detail in error_details]


def to_api_exception(exc: Exception):
    if isinstance(exc, Http404):
        return exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        return exceptions.PermissionDenied()
    elif not isinstance(exc, exceptions.APIException):
        return exceptions.APIException()

    return exc


def log_exception(exception: Exception, logger: Logger):
    logger.exception(
        f"Caught an exception, name={exception.__class__.__name__}",
        exc_info=True,
        extra={
            "exception": {
                "name": exception.__class__.__name__,
            },
        },
    )
