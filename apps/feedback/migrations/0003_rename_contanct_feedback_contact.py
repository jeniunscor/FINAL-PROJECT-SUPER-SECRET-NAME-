# Generated by Django 4.2 on 2023-05-27 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='contanct',
            new_name='contact',
        ),
    ]