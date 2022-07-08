from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authorization.api.schemas import auth_response
from avia.api.schemas import response_400


@extend_schema(
    summary="Авторизация",
    description="Авторизация пользователя в системе",
    tags=["Authorization"],
    responses={
        200: auth_response,
        400: response_400,
    }
)
class AuthView(TokenObtainPairView):
    pass


@extend_schema(
    summary="Обновление токена доступа",
    description="Обновление токена доступа",
    tags=["Authorization"],
    responses={
        200: auth_response,
        400: response_400,
    }
)
class RefreshView(TokenRefreshView):
    pass
