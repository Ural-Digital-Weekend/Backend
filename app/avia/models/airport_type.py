from django.db.models import Model, CharField


class AirportType(Model):
    title = CharField('Наименование', max_length=255)

    class Meta:
        verbose_name = 'вид аэропорта'
        verbose_name_plural = 'виды аэропортов'

    def __str__(self):
        return self.title
