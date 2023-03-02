# Generated by Django 4.1.7 on 2023-03-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0004_rename_name_event_event_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="event_date",
            new_name="event_time",
        ),
        migrations.RemoveField(
            model_name="event",
            name="event_times",
        ),
        migrations.AddField(
            model_name="event",
            name="event_duration",
            field=models.TimeField(null=True, verbose_name="event duration"),
        ),
        migrations.AddField(
            model_name="event",
            name="event_end_time",
            field=models.TimeField(max_length=20, null=True),
        ),
    ]