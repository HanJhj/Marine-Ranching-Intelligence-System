# Generated by Django 4.2.13 on 2024-06-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BackManage", "0002_device"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ShowUser",
        ),
        migrations.AlterField(
            model_name="device",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
