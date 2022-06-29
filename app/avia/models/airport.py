from django.db.models import Model, CharField, ForeignKey, CASCADE


class Airport(Model):
    ident = CharField('Идентификатор', max_length=10, unique=True)
    local_code = CharField('Код', max_length=10, blank=True, null=True)
    name = CharField('Наименование', max_length=255)

    coordinates = CharField(blank=True, null=True, max_length=255)
    elevation_ft = CharField(blank=True, null=True, max_length=255)
    gps_code = CharField(blank=True, null=True, max_length=255)
    iata_code = CharField(blank=True, null=True, max_length=10)

    continent = ForeignKey('avia.Continent', verbose_name='Континент', on_delete=CASCADE, related_name='airport', blank=True, null=True)
    type = ForeignKey('avia.AirportType', verbose_name='Тип аэропорта', on_delete=CASCADE, related_name='airport', blank=True, null=True)
    country = ForeignKey('avia.Country', verbose_name='Страна', on_delete=CASCADE, related_name='airport', blank=True, null=True)
    region = ForeignKey('avia.Region', verbose_name='Регион', on_delete=CASCADE, related_name='airport', blank=True, null=True)
    municipality = ForeignKey('avia.Municipality', verbose_name='Город', on_delete=CASCADE, related_name='airport', blank=True, null=True)

    class Meta:
        verbose_name = 'аэропорт'
        verbose_name_plural = 'аэропорты'

    def __str__(self):
        return f'{self.name} ({self.local_code} - {self.ident})'
