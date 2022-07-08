from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from avia.api.schemas.parameters import search_parameter
from avia.api.schemas.responses import response_200_handbooks
from avia.models import Region
from avia.serializers.handbooks.region import RegionSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Получение перечня регионов",
        tags=['Handbooks'],
        parameters=[
            search_parameter,
        ],
        responses={
            200: response_200_handbooks,
        }
    ),
)
class RegionsViewSet(ModelViewSet):
    authentication_classes = []
    filter_backends = [SearchFilter]
    search_fields = ['iso_code']
    pagination_class = None

    queryset = Region.objects
    serializer_class = RegionSerializer
