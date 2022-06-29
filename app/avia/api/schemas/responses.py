from drf_spectacular.utils import OpenApiResponse, inline_serializer, OpenApiExample
from rest_framework import serializers

response_200 = OpenApiResponse(
    description="Успешно получено"
)

response_200_list = OpenApiResponse(
    response=serializers.ListSerializer(child=serializers.CharField()),
)

response_201 = OpenApiResponse(
    description='Успешно добавлено',
)

response_204 = OpenApiResponse(
    description='Успешно удалено'
)

response_400 = OpenApiResponse(
    description='Неверный запрос',
    response=inline_serializer(
        name='BadRequestSerializer',
        fields={
            'detail': serializers.CharField(),
        }
    ),
    examples=[
        OpenApiExample(
            'Пример',
            value={
                "detail": "Был отправлен некорректный запрос"
            }
        )
    ]
)

response_401 = OpenApiResponse(
    description='Пользователь не авторизован',
    response=inline_serializer(
        name='UnAuthSerializer',
        fields={
            'detail': serializers.CharField(),
        }
    ),
    examples=[
        OpenApiExample(
            'Пример',
            value={
                "detail": "У вас недостаточно прав для выполнения данного действия."
            }
        )
    ]
)

response_404 = OpenApiResponse(
    description='Ресурс не найден',
    response=inline_serializer(
        name='NotFoundSerializer',
        fields={
            'detail': serializers.CharField(),
        }
    ),
)
