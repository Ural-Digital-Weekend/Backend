from django.urls import path
from rest_framework import routers

from avia.views import AirportsViewSet, AirportTypesViewSet, CommentsViewSet, ContinentsViewSet, CountriesViewSet, \
    MunicipalitiesViewSet, RegionsViewSet

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('airports', AirportsViewSet.as_view({
        'get': 'list'
    })),

    path('airports/<int:pk>', AirportsViewSet.as_view({
        'get': 'retrieve'
    })),

    path('airports/<int:airport_id>/comments', CommentsViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('airports/comments/<int:pk>', CommentsViewSet.as_view({
        'put': 'update',
        'delete': 'remove'
    })),

    path('handbooks/airport-types', AirportTypesViewSet.as_view({
        'get': 'list'
    })),

    path('handbooks/regions', RegionsViewSet.as_view({
        'get': 'list'
    })),

    path('handbooks/countries', CountriesViewSet.as_view({
        'get': 'list'
    })),

    path('handbooks/continents', ContinentsViewSet.as_view({
        'get': 'list'
    })),

    path('handbooks/municipalities', MunicipalitiesViewSet.as_view({
        'get': 'list'
    })),
])
