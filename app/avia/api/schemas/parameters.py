from drf_spectacular.utils import OpenApiParameter, OpenApiExample

pagination_parameters = [
    OpenApiParameter(
        location=OpenApiParameter.QUERY,
        name='count',
        description='Количество элементов на странице',
        required=False,
    ),
    OpenApiParameter(
        location=OpenApiParameter.QUERY,
        name='page',
        description='Номер страницы',
        required=False,
    )
]

order_parameter = OpenApiParameter(
    location=OpenApiParameter.QUERY,
    name='ordering',
    description='Поле, по которому производится сортировка',
    required=False,
    examples=[
        OpenApiExample(
            'Идентификатор (по возрастанию)',
            value='id'
        ),
        OpenApiExample(
            'Идентификатор (по убыванию)',
            value='-id'
        ),
    ],
)

search_parameter = OpenApiParameter(
    location=OpenApiParameter.QUERY,
    name='search',
    description='Текстовый поиск',
)