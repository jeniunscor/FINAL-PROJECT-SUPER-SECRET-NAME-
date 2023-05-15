from django.db.models import TextChoices


class GenderType(TextChoices):
    MAlE = 'MAlE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
