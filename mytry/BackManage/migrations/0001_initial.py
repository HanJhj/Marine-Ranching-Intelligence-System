# Generated by Django 4.2.13 on 2024-06-19 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShowUser",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=150)),
                ("password", models.CharField(max_length=128)),
                ("email", models.CharField(max_length=254)),
                ("is_superuser", models.SmallIntegerField(default=0)),
                ("is_staff", models.SmallIntegerField(default=0)),
            ],
            options={
                "db_table": "show_user",
                "managed": False,
            },
        ),
    ]
