# Generated by Django 2.2.12 on 2022-12-13 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_student_kuna'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email_studenta',
        ),
        migrations.RemoveField(
            model_name='student',
            name='kuna',
        ),
    ]