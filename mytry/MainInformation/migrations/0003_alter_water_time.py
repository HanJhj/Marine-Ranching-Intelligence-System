# Generated by Django 4.2.13 on 2024-06-22 03:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MainInformation", "0002_alter_water_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="water",
            name="time",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
