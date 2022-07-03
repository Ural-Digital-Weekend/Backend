from rest_framework.serializers import ModelSerializer

from avia.models import Country


class CountrySerializer(ModelSerializer):
    def to_representation(self, instance):
        return instance.iso_code

    class Meta:
        model = Country
        fields = [
            "iso_code",
        ]
