# Generated by Django 4.2 on 2023-05-27 16:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=55, verbose_name='заголовок')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='подзаголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание поста')),
                ('realty_type', models.CharField(choices=[('ПРОДАЖА', 'Продажа'), ('АРЕНДА', 'Аренда')], default='ПРОДАЖА', max_length=10, verbose_name='тип выдачи')),
                ('is_active', models.BooleanField(default=False, verbose_name='активный пост')),
                ('address', models.CharField(max_length=255, verbose_name='адресс')),
                ('area', models.CharField(max_length=85, verbose_name='площадь')),
                ('room_number', models.PositiveIntegerField(default=1, verbose_name='количество комнат')),
                ('floor', models.CharField(blank=True, max_length=85, null=True, verbose_name='этаж')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='цена')),
                ('phone_number', models.CharField(max_length=80, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.FileField(upload_to='post_images/%Y/%m/%d/', verbose_name='картинка')),
                ('is_preview', models.BooleanField(default=False, verbose_name='Превью')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
    ]
