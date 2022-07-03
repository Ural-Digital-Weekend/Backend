from rest_framework.serializers import ModelSerializer

from avia.models import Continent


class ContinentSerializer(ModelSerializer):
    def to_representation(self, instance):
        return instance.title

    class Meta:
        model = Continent
        fields = [
            "title",
        ]
