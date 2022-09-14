# Generated by Django 4.1 on 2022-09-14 14:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import videos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="عنوان")),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        blank=True,
                        unique=True,
                        verbose_name="عنوان برای URL",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="videos.category",
                        verbose_name="زیر دسته بندی",
                    ),
                ),
            ],
            options={
                "verbose_name": "دسته بندی",
                "verbose_name_plural": "دسته بندی ها",
            },
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="عنوان")),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        blank=True,
                        unique=True,
                        verbose_name="عنوان برای URL",
                    ),
                ),
                ("views", models.IntegerField(default=0, verbose_name="بازدیدها")),
                (
                    "video",
                    models.FileField(
                        upload_to=videos.models.create_videos_path,
                        verbose_name="فایل ویدئو",
                    ),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=videos.models.create_cover_image_path,
                        verbose_name="کاور ویدئو",
                    ),
                ),
                ("duration", models.DurationField(verbose_name="طول ویدئو")),
                ("description", ckeditor.fields.RichTextField(verbose_name="توضیحات")),
                ("published_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="videos.category",
                        verbose_name="دسته بندی",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="teachers.teacher",
                        verbose_name="استاد",
                    ),
                ),
            ],
            options={
                "verbose_name": "ویدئو",
                "verbose_name_plural": "ویدئو ها",
            },
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("liked_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="videos.video",
                        verbose_name="ویدئو",
                    ),
                ),
            ],
            options={
                "verbose_name": "لایک",
                "verbose_name_plural": "لایک ها",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField(verbose_name="کامنت")),
                ("commented_at", models.DateTimeField(auto_now_add=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="videos.comment",
                        verbose_name="پاسخ به",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="videos.video",
                        verbose_name="ویدئو",
                    ),
                ),
            ],
            options={
                "verbose_name": "کامنت",
                "verbose_name_plural": "کامنت ها",
            },
        ),
    ]
