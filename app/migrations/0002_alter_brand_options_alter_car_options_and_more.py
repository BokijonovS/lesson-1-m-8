# Generated by Django 5.0.6 on 2024-06-12 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '1. Brand.'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name_plural': '3. Cars.'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': '2. Colors.'},
        ),
    ]
