import uuid
from django.db import models

from apps.common.constant import RealtyType
from apps.common.models import AbstractBaseModel
from apps.users.models import User


class Category(AbstractBaseModel):
    name = models.CharField(
        max_length=70, verbose_name="название",
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(AbstractBaseModel):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=uuid.uuid4
    )
    title = models.CharField(
        max_length=55, verbose_name='заголовок',
    )
    subtitle = models.CharField(
        max_length=100, verbose_name='подзаголовок',
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='posts',
        verbose_name='категория'
    )
    description = models.TextField(
        blank=True, null=True, verbose_name='описание поста'
    )
    realty_type = models.CharField(
        max_length=10, choices=RealtyType.choices,
        verbose_name='тип выдачи',
        default=RealtyType.ПРОДАЖА
    )
    is_active = models.BooleanField(
        default=False, verbose_name='активный пост'
    )
    commentary = models.ForeignKey(
        'Commentary', on_delete=models.CASCADE, null=True, blank=True,
        related_name='posts', verbose_name='комментарий'
    )
    post_image = models.ForeignKey(
        'PostImage', on_delete=models.CASCADE, null=True, blank=True,
        related_name='posts', verbose_name='картина'
    )
    address = models.CharField(
        max_length=255, verbose_name='адресс'
    )
    area = models.CharField(
        max_length=85, verbose_name='площадь'
    )
    room_number = models.PositiveIntegerField(
        default=1, verbose_name='количество комнат'
    )
    floor = models.CharField(
        max_length=85, verbose_name='этаж',
        blank=True, null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='цена'
    )
    phone_number = models.CharField(
        max_length=80, verbose_name='номер телефона'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class PostImage(AbstractBaseModel):
    photo = models.FileField(
        upload_to='post_images/%Y/%m/%d/',
        verbose_name='картинка'
    )
    is_preview = models.BooleanField(
        default=False, verbose_name='Превью'
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Commentary(AbstractBaseModel):
    author = models.ForeignKey(
        'users.User', on_delete=models.CASCADE,
        related_name='commentaries', verbose_name='автор'
    )
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, null=True, blank=True,
        related_name='comments', verbose_name='пост'
    )
    description = models.TextField(
        blank=True, null=True, verbose_name='описание'
    )
    is_active = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.author.username
