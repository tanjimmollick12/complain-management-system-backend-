# Generated by Django 4.0.3 on 2022-04-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_username_user_is_admin_user_nsu_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nsu_id',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30, verbose_name='username'),
        ),
    ]
