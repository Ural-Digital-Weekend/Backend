from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from avia.models import Continent


class ContinentsViewSet(ModelViewSet):
    permission_classes = []
    queryset = Continent.objects

    def list(self, request, *args, **kwargs):
        return Response(data=dict(self.queryset.values_list("id", "title")), status=status.HTTP_200_OK)