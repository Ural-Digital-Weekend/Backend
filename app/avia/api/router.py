from django.urls import path
from rest_framework import routers

from avia.views.airports import AirportsViewSet

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('airports', AirportsViewSet.as_view({
        'get': 'list'
    })),

    path('airports/<int:pk>', AirportsViewSet.as_view({
        'get': 'retrieve'
    })),
])
