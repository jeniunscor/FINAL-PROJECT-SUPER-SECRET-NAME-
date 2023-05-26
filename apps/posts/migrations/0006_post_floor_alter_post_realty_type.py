# Generated by Django 4.2 on 2023-05-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='floor',
            field=models.CharField(blank=True, max_length=85, null=True, verbose_name='этаж'),
        ),
        migrations.AlterField(
            model_name='post',
            name='realty_type',
            field=models.CharField(choices=[('ПРОДАЖА', 'Продажа'), ('АРЕНДА', 'Аренда')], default='ПРОДАЖА', max_length=10, verbose_name='тип выдачи'),
        ),
    ]