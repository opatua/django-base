from rest_framework.renderers import JSONRenderer


class CustomJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {"data": data if data is not None else {}}
        if isinstance(data, dict) and "data" in data.keys():
            response_data = data

        return super().render(response_data, accepted_media_type, renderer_context)
