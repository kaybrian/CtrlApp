# Generated by Django 3.2.8 on 2023-11-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_auto_20231127_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitytimetable',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='availabilitytimetable',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]