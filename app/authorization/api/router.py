from django.urls import path
from rest_framework import routers

from authorization.views import RegistrationVIew
from authorization.views.auth import AuthView, RefreshView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('login', AuthView.as_view(), name='login'),
    path('refresh', RefreshView.as_view(), name='refresh'),
    path('register', RegistrationVIew.as_view(), name='register'),
])
