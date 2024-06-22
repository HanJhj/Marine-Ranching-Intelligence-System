# Generated by Django 4.2.13 on 2024-06-22 00:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BackManage", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("state", models.SmallIntegerField(default=0)),
            ],
        ),
    ]
