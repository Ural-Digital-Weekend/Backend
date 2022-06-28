from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from avia.models import Comment


class UserEmailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class CommentListSerializer(ModelSerializer):
    user = UserEmailSerializer()

    class Meta:
        model = Comment
        fields = (
            "id",
            "user",
            "created",
            "comment",
        )
