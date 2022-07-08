from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from avia.api.schemas.parameters import search_parameter
from avia.api.schemas.responses import response_200_handbooks
from avia.models import AirportType
from avia.serializers import AirportTypeSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Получение перечня типов аэропортов",
        tags=['Handbooks'],
        parameters=[
            search_parameter,
        ],
        responses={
            200: response_200_handbooks,
        }
    ),
)
class AirportTypesViewSet(ModelViewSet):
    authentication_classes = []
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = None

    queryset = AirportType.objects
    serializer_class = AirportTypeSerializer
