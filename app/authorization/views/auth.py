from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authorization.api.schemas import auth_responses


@extend_schema(
    summary="Авторизация",
    description="Авторизация пользователя в системе",
    tags=["Authorization"],
    responses=auth_responses
)
class AuthView(TokenObtainPairView):
    pass


@extend_schema(
    summary="Обновление токена доступа",
    description="Обновление токена доступа",
    tags=["Authorization"],
    responses=auth_responses
)
class RefreshView(TokenRefreshView):
    pass
