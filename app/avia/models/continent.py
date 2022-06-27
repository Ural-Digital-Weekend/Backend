from django.db.models import Model, CharField


class Continent(Model):
    title = CharField('Наименование', max_length=255)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.title
