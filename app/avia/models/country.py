from django.db.models import Model, CharField


class Country(Model):
    iso_code = CharField('Код страны', max_length=2)
