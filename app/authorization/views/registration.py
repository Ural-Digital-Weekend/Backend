from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from authorization.api.schemas import auth_responses
from authorization.serializers import UserSerializer
from authorization.utils import get_tokens_for_user


class RegistrationVIew(APIView):
    authentication_classes = []

    @extend_schema(
        summary="Регистрация",
        description="Регистрация пользователя в системе",
        tags=["Authorization"],
        request=inline_serializer(
            name='AuthSerializer',
            fields={
                'username': serializers.CharField(),
                'email': serializers.EmailField(),
                'password': serializers.CharField(),
            },
        ),
        responses=auth_responses
    )
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
