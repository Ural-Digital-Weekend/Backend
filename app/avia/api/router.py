from django.urls import path
from rest_framework import routers

from avia.views import AirportsViewSet, AirportTypesViewSet
from avia.views.handbooks.continent import ContinentsViewSet
from avia.views.handbooks.countries import CountriesViewSet
from avia.views.handbooks.municipality import MunicipalitiesViewSet
from avia.views.handbooks.regions import RegionsViewSet

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns.extend([
    path('airports', AirportsViewSet.as_view({
        'get': 'list'
    })),

    path('airports/<int:pk>', AirportsViewSet.as_view({
        'get': 'retrieve'
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
