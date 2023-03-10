# Generated by Django 2.2.12 on 2022-12-12 18:45

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20221212_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='maturant',
            name='maturant_datum_upisa',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='student_datum_upisa',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='maturant',
            name='upisni_broj',
            field=models.IntegerField(default=10000, help_text='value 10 000 to 99 999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='mjesto',
            name='postanski_broj',
            field=models.IntegerField(default=10000, help_text='value 10 000 to 99 999', validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='jmbag_studenta',
            field=models.IntegerField(validators=[main.models.validate_10_digits]),
        ),
    ]
