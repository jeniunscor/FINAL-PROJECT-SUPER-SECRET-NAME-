from django.db import models
from apps.common.models import AbstractBaseModel


class Faq(AbstractBaseModel):
    question = models.CharField(
        max_length=200, verbose_name='Вопрос'
    )
    answer = models.TextField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return f'{self.question} - {self.answer}'