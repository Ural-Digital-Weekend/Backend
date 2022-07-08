from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from avia.api.schemas.parameters import search_parameter
from avia.api.schemas.responses import response_200_handbooks
from avia.models import Municipality
from avia.serializers.handbooks.municipality import MunicipalitySerializer


@extend_schema_view(
    list=extend_schema(
        summary="Получение перечня городов",
        tags=['Handbooks'],
        parameters=[
            search_parameter,
        ],
        responses={
            200: response_200_handbooks,
        }
    ),
)
class MunicipalitiesViewSet(ModelViewSet):
    authentication_classes = []
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = None

    queryset = Municipality.objects
    serializer_class = MunicipalitySerializer
