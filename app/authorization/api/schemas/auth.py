from drf_spectacular.utils import OpenApiResponse, inline_serializer
from rest_framework import serializers

auth_response = OpenApiResponse(
    response=inline_serializer(
        name='AuthSerializer',
        fields={
            'access': serializers.CharField(),
            'refresh': serializers.CharField(),
        },
    ),
)
