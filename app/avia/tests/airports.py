from django.test import TestCase

from django.core.management import call_command
from rest_framework.test import APIClient

from avia.models import Airport


class AirportsTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super(AirportsTest, cls).setUpClass()
        call_command('refill_avia_data')

    def setUp(self) -> None:
        self.client = APIClient()
        self.routes = {
            'list': '/api/airports',
            'detail': '/api/airports/{airport_id}'
        }

    def test_get_airports_list(self):
        airport = Airport.objects.order_by('name').first()

        response = self.client.get(self.routes['list'])

        self.assertEqual(200, response.status_code)
        self.assertEqual(Airport.objects.count(), response.data.get('count'))
        self.assertEqual(airport.id, response.data.get('results')[0]['id'])
        self.assertEqual(airport.name, response.data.get('results')[0]['name'])

    def test_get_airport_detail(self):
        airport = Airport.objects.order_by('name').first()

        response = self.client.get(self.routes['detail'].format(airport_id=airport.id))

        self.assertEqual(200, response.status_code)
        self.assertEqual(airport.ident, response.data.get('ident'))
        self.assertEqual(airport.name, response.data.get('name'))
