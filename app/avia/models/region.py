from django.db.models import Model, CharField


class Region(Model):
    iso_code = CharField('Код региона', max_length=10)
