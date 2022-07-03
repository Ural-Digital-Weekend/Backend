from rest_framework.serializers import ModelSerializer

from avia.models import Region


class RegionSerializer(ModelSerializer):
    def to_representation(self, instance):
        return instance.iso_code

    class Meta:
        model = Region
        fields = [
            "iso_code",
        ]
