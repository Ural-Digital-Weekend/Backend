from django.db.models import Model, CharField


class Country(Model):
    iso_code = CharField('Код страны', max_length=2)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.iso_code
