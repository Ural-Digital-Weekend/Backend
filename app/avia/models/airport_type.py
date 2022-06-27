from django.db.models import Model, CharField


class AirportType(Model):
    title = CharField('Наименование', max_length=255)
