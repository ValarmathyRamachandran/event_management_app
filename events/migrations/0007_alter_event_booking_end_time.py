# Generated by Django 4.2.1 on 2023-07-01 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_booking_end_time_event_booking_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='booking_end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 8, 12, 12, 48, 37874, tzinfo=datetime.timezone.utc)),
        ),
    ]
