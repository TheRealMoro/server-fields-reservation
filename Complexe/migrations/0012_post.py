# Generated by Django 4.1.7 on 2023-04-20 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Complexe', '0011_alter_reservation_date_alter_reservation_endtime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number_of_players_needed', models.IntegerField()),
                ('number_of_players_available', models.IntegerField()),
                ('description', models.TextField()),
                ('post_reservation', models.ManyToManyField(blank=True, to='Complexe.reservation')),
                ('terrain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Complexe.terrain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
