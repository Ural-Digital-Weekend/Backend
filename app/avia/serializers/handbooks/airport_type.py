from rest_framework.serializers import ModelSerializer

from avia.models import AirportType


class AirportTypeSerializer(ModelSerializer):
    def to_representation(self, instance):
        return instance.title

    class Meta:
        model = AirportType
        fields = [
            "title",
        ]
