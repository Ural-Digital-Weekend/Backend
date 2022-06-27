from django.db.models import Model, CharField


class Municipality(Model):
    title = CharField('Наименование', max_length=255)
