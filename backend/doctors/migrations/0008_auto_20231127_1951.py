# Generated by Django 3.2.8 on 2023-11-27 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_auto_20231127_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilitytimetable',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availabilitytimetable',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
