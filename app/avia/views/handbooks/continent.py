from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from avia.api.schemas.parameters import search_parameter
from avia.api.schemas.responses import response_200_handbooks
from avia.models import Continent
from avia.serializers import ContinentSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Получение перечня континентов",
        tags=['Handbooks'],
        parameters=[
            search_parameter,
        ],
        responses={
            200: response_200_handbooks,
        }
    ),
)
class ContinentsViewSet(ModelViewSet):
    authentication_classes = []
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = None

    queryset = Continent.objects
    serializer_class = ContinentSerializer
