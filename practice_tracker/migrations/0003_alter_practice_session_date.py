# Generated by Django 4.1 on 2022-08-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_tracker', '0002_practice_session_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice_session',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
