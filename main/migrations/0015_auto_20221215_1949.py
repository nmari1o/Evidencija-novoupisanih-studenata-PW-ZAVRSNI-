# Generated by Django 2.2.12 on 2022-12-15 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20221215_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smjer',
            old_name='smjer_fakulteti',
            new_name='fakulteti',
        ),
    ]
