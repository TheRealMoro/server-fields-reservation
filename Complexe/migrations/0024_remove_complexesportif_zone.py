# Generated by Django 4.1.7 on 2023-05-18 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Complexe', '0023_complexesportif_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complexesportif',
            name='zone',
        ),
    ]
