from rest_framework.serializers import ModelSerializer

from authorization.serializers import UserSerializer
from avia.models import Comment


class CommentListSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "created",
            "comment",
        )
