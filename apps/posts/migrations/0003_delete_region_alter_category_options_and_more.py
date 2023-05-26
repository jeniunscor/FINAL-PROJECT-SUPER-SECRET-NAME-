# Generated by Django 4.2 on 2023-05-23 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='commentary',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AlterModelOptions(
            name='postimage',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.postimage', verbose_name='картина'),
        ),
        migrations.AlterField(
            model_name='post',
            name='room_number',
            field=models.PositiveIntegerField(default=1, verbose_name='количество комнат'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='photo',
            field=models.FileField(upload_to='post_images/%Y/%m/%d/', verbose_name='картинка'),
        ),
    ]