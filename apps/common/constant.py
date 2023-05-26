from django.db.models import TextChoices


class GenderType(TextChoices):
    МУЖСКОЙ = 'МУЖСКОЙ'
    ЖЕНСКИЙ = 'ЖЕНСКИЙ'
    ДРУГИЕ = 'ДРУГИЕ'


class RealtyType(TextChoices):
    ПРОДАЖА = 'ПРОДАЖА'
    АРЕНДА = 'АРЕНДА'


class UserType(TextChoices):
    ПРОДАВЕЦ = 'ПРОДАВЕЦ'
    ПОКУПАТЕЛЬ = 'ПОКУПАТЕЛЬ'
    ГОСТЬ = 'ГОСТЬ'
