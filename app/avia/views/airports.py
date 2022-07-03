from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view, OpenApiParameter
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from avia.api.schemas import response_400
from avia.api.schemas.parameters import order_parameter, pagination_parameters
from avia.models import Airport
from avia.serializers import AirportSerializer, AirportListElementSerializer


@extend_schema_view(
    retrieve=extend_schema(
        summary="Получение сведений об аэропорте",
        tags=['Airports'],
        parameters=[
            OpenApiParameter(
                location=OpenApiParameter.PATH,
                name='id',
                description='идентификатор аэропорта',
                required=True,
            ),
        ],
        responses={
            200: AirportSerializer,
        }
    ),
)
class AirportsViewSet(ModelViewSet):
    authentication_classes = []
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ('id', 'ident', 'local_code', 'name',)  # Перечень полей, по которым можно осуществлять фильтрацию
    ordering_fields = ('id', 'ident', 'local_code', 'name',)  # Перечень полей, по которым доступна сортировка
    ordering = ('name',)  # Сортировка по умолчанию

    queryset = Airport.objects
    serializer_class = AirportSerializer

    def filter_queryset(self, queryset):
        qs = super(AirportsViewSet, self).filter_queryset(queryset)
        filter_fields = {
            "type__title": self.request.query_params.get('type', None),
            "continent__title": self.request.query_params.get('continent', None),
            "municipality__title": self.request.query_params.get('municipality', None),
            "country__iso_code": self.request.query_params.get('country', None),
            "region__iso_code": self.request.query_params.get('region', None),
        }

        return qs.filter(*[
            Q(filter_item) for filter_item in filter_fields.items() if filter_item[1] is not None
        ])

    @extend_schema(
        summary="Получение данных об аэропротах",
        tags=['Airports'],
        parameters=[
            order_parameter,
            *pagination_parameters,
            OpenApiParameter(
                location=OpenApiParameter.QUERY,
                name='search',
                description='Текстовый поиск по полям id, ident, local_code, name',
            ),
            OpenApiParameter(
                location=OpenApiParameter.QUERY,
                name='type',
                description='тип аэропорта',
            ),
            OpenApiParameter(
                location=OpenApiParameter.QUERY,
                name='continent',
                description='континент',
            ),
            OpenApiParameter(
                location=OpenApiParameter.QUERY,
                name='municipality',
                description='город',
            ),
            OpenApiParameter(
                location=OpenApiParameter.QUERY,
                name='country',
                description='страна',
            ),
        ],
        responses={
            200: OpenApiResponse(
                description="Успешно получен список заказанных выписок",
                response=AirportListElementSerializer,
            ),
            400: response_400,
        }
    )
    def list(self, request, *args, **kwargs):
        self.serializer_class = AirportListElementSerializer
        return super(AirportsViewSet, self).list(request, *args, **kwargs)
