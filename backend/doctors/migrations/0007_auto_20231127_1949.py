# Generated by Django 3.2.8 on 2023-11-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_auto_20231127_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitytimetable',
            name='end_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='availabilitytimetable',
            name='start_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]