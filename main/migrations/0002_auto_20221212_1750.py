# Generated by Django 2.2.12 on 2022-12-12 17:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mjesto',
            name='postanski_broj',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='jmbag_studenta',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
