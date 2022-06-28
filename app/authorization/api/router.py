from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authorization.views import RegistrationVIew
from avia.views import AirportsViewSet, AirportTypesViewSet, CommentsViewSet, ContinentsViewSet, CountriesViewSet, \
    MunicipalitiesViewSet, RegionsViewSet

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('register', RegistrationVIew.as_view(), name='register'),
])
