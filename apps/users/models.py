from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


from apps.common.constant import GenderType
from apps.common.models import AbstractBaseModel


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class Region(AbstractBaseModel):
    name = models.CharField(
       max_length=100, verbose_name='Область'
    )
    parent = models.ForeignKey(
       'self', on_delete=models.CASCADE,
        related_name='children', blank=True, null=True,
        verbose_name='Родительская категория'
    )


class User(AbstractUser, AbstractBaseModel):
    username = models.CharField(
        max_length=25, blank=True,
        null=True, verbose_name='Логин',
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=60, unique=True,
    )
    avatar = models.FileField(
        upload_to='images/%Y/%m/%d/', 
        verbose_name='Фото'
    )
    # region = models.ForeignKey(
    #    Region, on_delete=models.CASCADE, related_name="User",
    #    verbose_name="Регион"
    # )
    number = models.CharField(
       max_length=50, verbose_name='Номер телефона'
    )
    gender = models.CharField(
        max_length=10, choices=GenderType.choices,
        verbose_name='Гендер пользователя', default=GenderType.FEMALE
    )
    is_admin = models.BooleanField(
       default=False,
    )
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
