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

    @extend_schema(
        summary="Получение данных об аэропротах",
        tags=['Airports'],
        parameters=[
            order_parameter,
            *pagination_parameters
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
