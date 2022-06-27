from django.db.models import Model, CharField


class Municipality(Model):
    title = CharField('Наименование', max_length=255)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.title
