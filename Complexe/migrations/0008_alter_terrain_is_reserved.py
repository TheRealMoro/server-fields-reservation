# Generated by Django 4.1.7 on 2023-04-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complexe', '0007_alter_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terrain',
            name='is_reserved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]