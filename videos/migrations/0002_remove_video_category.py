# Generated by Django 4.1 on 2022-09-14 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="category",
        ),
    ]
