# Generated by Django 4.0.5 on 2022-06-26 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airport',
            options={'verbose_name': 'аэропорт', 'verbose_name_plural': 'аэропорты'},
        ),
        migrations.AlterModelOptions(
            name='airporttype',
            options={'verbose_name': 'вид аэропорта', 'verbose_name_plural': 'виды аэропортов'},
        ),
        migrations.AlterModelOptions(
            name='continent',
            options={'verbose_name': 'страна', 'verbose_name_plural': 'страны'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'страна', 'verbose_name_plural': 'страны'},
        ),
        migrations.AlterModelOptions(
            name='municipality',
            options={'verbose_name': 'город', 'verbose_name_plural': 'города'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'регион', 'verbose_name_plural': 'регионы'},
        ),
    ]