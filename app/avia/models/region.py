from django.db.models import Model, CharField


class Region(Model):
    iso_code = CharField('Код региона', max_length=10)

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'

    def __str__(self):
        return self.iso_code
