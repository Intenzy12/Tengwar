# Generated by Django 4.1.7 on 2023-04-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0008_remove_event_num_registered_organization"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="hours_rewarded",
            field=models.IntegerField(default=0),
        ),
    ]
