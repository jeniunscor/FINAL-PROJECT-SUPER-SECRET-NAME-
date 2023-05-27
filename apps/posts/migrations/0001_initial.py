# Generated by Django 4.2 on 2023-05-26 08:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=70, verbose_name="название")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Commentary",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="описание"),
                ),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Коментарий",
                "verbose_name_plural": "Коментарии",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=55, verbose_name="заголовок")),
                (
                    "subtitle",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="подзаголовок",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание поста"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="активный пост"),
                ),
                ("address", models.CharField(max_length=255, verbose_name="адресс")),
                ("area", models.CharField(max_length=85, verbose_name="площадь")),
                (
                    "room_number",
                    models.IntegerField(default=1, verbose_name="количество комнат"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="цена"
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=80, verbose_name="номер телефона"),
                ),
                (
                    "realty_type",
                    models.CharField(
                        choices=[
                            ("АРЕНДА", "Аренда"),
                            ("ПРОДАЖА", "Продажа"),
                            ("ПОКУПКА", "Покупка"),
                        ],
                        default="ПРОДАЖА",
                        max_length=10,
                        verbose_name="вид приобретение",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="posts.category",
                        verbose_name="категория",
                    ),
                ),
                (
                    "commentary",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="posts.commentary",
                        verbose_name="комментарий",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.CreateModel(
            name="PostImage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "photo",
                    models.FileField(
                        upload_to="post_images/%Y/%m/%d/", verbose_name="рисунок"
                    ),
                ),
                (
                    "is_preview",
                    models.BooleanField(default=False, verbose_name="Превью"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_images",
                        to="posts.post",
                        verbose_name="Пост",
                    ),
                ),
            ],
            options={
                "verbose_name": "Картинка",
                "verbose_name_plural": "Картинки",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="post_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="posts.postimage",
                verbose_name="рисунок",
            ),
        ),
    ]
