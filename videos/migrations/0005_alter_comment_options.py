# Generated by Django 4.1 on 2022-09-18 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0004_alter_video_viewers_by_ip"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-commented_at"],
                "verbose_name": "کامنت",
                "verbose_name_plural": "کامنت ها",
            },
        ),
    ]