from django.db import models

from apps.common.models import AbstractBaseModel
from apps.users.models import User
from apps.posts.models import Post


class Feedback(AbstractBaseModel):
    user = models.ForeignKey(
        User, related_name='feedbacks',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    name = models.CharField(
        max_length=25, verbose_name='Имя'
    )
    contact = models.CharField(
        max_length=9, verbose_name='Контакты'
    )
    message = models.TextField(
        verbose_name='Сообщение'
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'

    def __str__(self):
        return f'{self.user} - {self.name}'


class Favorite(AbstractBaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='favorited_by'
    )

    class Meta:
        unique_together = [['user', 'post']]
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'User {self.user.email} favorites post {self.post.id}'
