# from django.db import models


# class Category(models.Model):
#     name = models.CharField(
#         max_length=70, verbose_name="название",
#     )


# class Post(models.Model):
#     title = models.CharField(
#         max_length=55, verbose_name="заголовок",
#     )
#     subtitle = models.CharField(
#         max_length=100, verbose_name="подзаголовок",
#         blank=True, null=True
#     )
#     category = models.ForeignKey(
#         Category, on_delete=models.CASCADE, related_name="posts",
#         verbose_name="категория"
#     )
#     description = models.TextField(
#         blank=True, null=True,
#     )
#     is_active = models.BooleanField(
#         default=False
#     )
#     commentary = models.ForeignKey(
#         'Commentary', on_delete=models.CASCADE, null=True, blank=True,
#         related_name="posts", verbose_name="комментарий"
#     )
#     post_image = models.ForeignKey(
#         'Post_image', on_delete=models.CASCADE, null=True, blank=True,
#         related_name="posts", verbose_name="рисунок"
#     )
#     address = models.CharField(
#         max_length=255, verbose_name="адресс"
#     )
#     area = models.CharField(
#         max_length=85, verbose_name="площадь"
#     )
#     room_number = models.IntegerField(
#         default=0, verbose_name='количество комнат'
#     )
#     price = models.DecimalField(
#         max_digits=2, verbose_name="цена"
#     )
#     phone_number = models.CharField(
#         max_length=80, verbose_name="номер телефона"
#     )
#     realty_type = models.ChoiceField(

#     )
#     user_type = models.ChoiceField(

#     )


# class Region(models.Model):
#     name = models.CharField(
#         max_length=125, verbose_name="Название"
#     )


# class PostImage(models.Model):
#     photo = models.FileField(

#     )


# class Commentary(models.Model):
#     author = models.ForeignKey(
#         'author', on_delete=models.CASCADE, null=True, blank=True,
#         related_name="users", verbose_name="автор"
#     )
#     description = models.TextField(
#         blank=True, null=True,
#     )
#     is_active = models.BooleanField(
#         default=False
#     )
