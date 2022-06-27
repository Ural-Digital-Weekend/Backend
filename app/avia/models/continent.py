from django.db.models import Model, CharField


class Continent(Model):
    title = CharField('Наименование', max_length=255)
