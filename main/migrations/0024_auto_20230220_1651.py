# Generated by Django 2.2.12 on 2023-02-20 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20230220_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='mjesto',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mjesto',
            name='postanski_broj',
            field=models.IntegerField(default=10000, help_text='value 10 000 to 99 999', unique=True, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)]),
        ),
    ]
