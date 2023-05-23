from django.db import models

from apps.common.constant import RealtyType
from apps.common.models import AbstractBaseModel


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
    title = models.CharField(
        max_length=55, verbose_name="заголовок",
    )
    subtitle = models.CharField(
        max_length=100, verbose_name="подзаголовок",
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts",
        verbose_name="категория"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name='описание поста'
    )
    is_active = models.BooleanField(
        default=False, verbose_name='активный пост'
    )
    commentary = models.ForeignKey(
        'Commentary', on_delete=models.CASCADE, null=True, blank=True,
        related_name="posts", verbose_name="комментарий"
    )
    post_image = models.ForeignKey(
        'PostImage', on_delete=models.CASCADE, null=True, blank=True,
        related_name="posts", verbose_name="рисунок"
    )
    address = models.CharField(
        max_length=255, verbose_name="адресс"
    )
    area = models.CharField(
        max_length=85, verbose_name="площадь"
    )
    room_number = models.IntegerField(
        default=1, verbose_name='количество комнат'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='цена'
    )
    phone_number = models.CharField(
        max_length=80, verbose_name="номер телефона"
    )
    realty_type = models.CharField(
        max_length=10, choices=RealtyType.choices,
        verbose_name='вид приобретение',
        default=RealtyType.ПРОДАЖА
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class PostImage(AbstractBaseModel):
    photo = models.FileField(
        upload_to='post_images/%Y/%m/%d/',
        verbose_name='рисунок'
    )
    post = models.ForeignKey(
        Post, related_name='post_images',
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    is_preview = models.BooleanField(
        default=False, verbose_name='Превью'
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.post


class Commentary(AbstractBaseModel):
    author = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, null=True, blank=True,
        related_name='users', verbose_name="автор"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="описание"
    )
    is_active = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.author
