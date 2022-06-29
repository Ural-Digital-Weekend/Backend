from drf_spectacular.utils import OpenApiResponse, inline_serializer
from rest_framework import serializers

from avia.api.schemas import response_400

auth_responses = {
    200: OpenApiResponse(
        response=inline_serializer(
            name='AuthSerializer',
            fields={
                'access': serializers.CharField(),
                'refresh': serializers.CharField(),
            },
        ),
    ),
    400: response_400
}
