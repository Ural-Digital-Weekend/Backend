from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from avia.models import Country


class CountriesViewSet(ModelViewSet):
    permission_classes = []
    queryset = Country.objects

    def list(self, request, *args, **kwargs):
        return Response(data=dict(self.queryset.values_list("id", "iso_code")), status=status.HTTP_200_OK)
