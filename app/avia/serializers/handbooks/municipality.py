from rest_framework.serializers import ModelSerializer

from avia.models import Municipality


class MunicipalitySerializer(ModelSerializer):
    def to_representation(self, instance):
        return instance.title

    class Meta:
        model = Municipality
        fields = [
            "title",
        ]
