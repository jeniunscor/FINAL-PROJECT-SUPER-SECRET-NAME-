from django.db import models

from apps.common.models import AbstractBaseModel
from apps.users.models import User


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
