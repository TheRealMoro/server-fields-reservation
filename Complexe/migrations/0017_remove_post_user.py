# Generated by Django 4.1.7 on 2023-04-20 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Complexe', '0016_remove_post_post_reservation_post_post_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]