# Generated by Django 4.2.4 on 2023-09-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_game', '0003_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_id',
        ),
        migrations.AlterField(
            model_name='game',
            name='game_string',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='game',
            name='is_palindrome',
            field=models.BooleanField(default=False),
        ),
    ]
