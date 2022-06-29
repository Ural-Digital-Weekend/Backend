# Generated by Django 4.0.5 on 2022-06-29 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avia', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='continent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.continent', verbose_name='Континент'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='municipality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.municipality', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.region', verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='airport',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='airport', to='avia.airporttype', verbose_name='Тип аэропорта'),
        ),
    ]
