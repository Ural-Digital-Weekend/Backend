from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authorization.api.schemas import auth_response
from authorization.serializers import UserSerializer
from avia.api.schemas import response_400


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
        responses={
            201: auth_response,
            400: response_400,
        }
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

        refresh = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data=data, status=status.HTTP_201_CREATED)
