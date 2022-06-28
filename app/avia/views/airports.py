from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from avia.models import Airport
from avia.serializers import AirportSerializer, AirportListElementSerializer


class AirportsViewSet(ModelViewSet):
    permission_classes = []
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ('id', 'ident', 'local_code', 'name',)  # Перечень полей, по которым можно осуществлять фильтрацию
    ordering_fields = ('id', 'ident', 'local_code', 'name',)  # Перечень полей, по которым доступна сортировка
    ordering = ('name',)  # Сортировка по умолчанию

    queryset = Airport.objects
    serializer_class = AirportSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = AirportListElementSerializer
        return super(AirportsViewSet, self).list(request, *args, **kwargs)
