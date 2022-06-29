from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from avia.models import Airport


class AirportListElementSerializer(ModelSerializer):
    region = StringRelatedField()
    country = StringRelatedField()
    type = StringRelatedField()

    class Meta:
        model = Airport
        fields = (
            "id",
            "name",
            "ident",
            "local_code",
            "region",
            "type",
            "country"
        )
