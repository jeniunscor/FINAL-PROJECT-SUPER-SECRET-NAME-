from django.db.models import TextChoices


class GenderType(TextChoices):
    МУЖСКОЙ = 'МУЖСКОЙ'
    ЖЕНСКИЙ = 'ЖЕНСКИЙ'
    ДРУГИЕ = 'ДРУГИЕ'


class RealtyType(TextChoices):
    АРЕНДА = 'АРЕНДА'
    ПРОДАЖА = 'ПРОДАЖА'
    ПОКУПКА = 'ПОКУПКА'


class UserType(TextChoices):
    ПРОДАВЕЦ = 'ПРОДАВЕЦ'
    ПОКУПАТЕЛЬ = 'ПОКУПАТЕЛЬ'
    ГОСТЬ = 'ГОСТЬ'
