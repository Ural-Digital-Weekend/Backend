from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from avia.api.schemas.responses import response_200_list
from avia.models import Region


class RegionsViewSet(ModelViewSet):
    authentication_classes = []
    queryset = Region.objects
    pagination_class = None

    @extend_schema(
        summary="Получение перечня регионов",
        tags=['Handbooks'],
        responses={
            200: response_200_list,
        }
    )
    def list(self, request, *args, **kwargs):
        return Response(data=self.queryset.values_list("iso_code", flat=True), status=status.HTTP_200_OK)
