# Generated by Django 4.2.1 on 2023-06-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
