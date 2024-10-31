from rest_framework.exceptions import ErrorDetail, ValidationError


class SignInValidationError(ValidationError):
    def __init__(self):
        super().__init__(
            ErrorDetail(
                "Email or Password is invalid.",
                __name__,
            ),
        )
