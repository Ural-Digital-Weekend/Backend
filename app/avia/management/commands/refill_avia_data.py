from django.core.management.base import BaseCommand

from avia.services import refill_db_avia_data


class Command(BaseCommand):
    help = 'Заполнить базу данных открытыми данными об аэропортах'

    def handle(self, *args, **kwargs):
        self.stdout.write("Заполнение данных об аэропортах", ending='\r')
        refill_db_avia_data('storage/airport-codes.csv')
        self.stdout.write("Заполнение данных об аэропортах - Готово")
