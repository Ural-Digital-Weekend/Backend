from rest_framework.serializers import ModelSerializer

from avia.models import Airport


class AirportListElementSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = (
            "id",
            "ident",
            "local_code",
            "name",
            "coordinates",
        )
