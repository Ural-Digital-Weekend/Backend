from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authorization.serializers import UserSerializer
from authorization.utils import get_tokens_for_user


class RegistrationVIew(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        user = User.objects.create_user(
            username=user.get('username'),
            email=user.get('email'),
            password=user.get('password'),
        )

        return Response(data=get_tokens_for_user(user), status=status.HTTP_201_CREATED)
