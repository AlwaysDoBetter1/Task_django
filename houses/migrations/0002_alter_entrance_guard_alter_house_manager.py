# Generated by Django 4.2.14 on 2024-07-29 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrance',
            name='guard',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Guard'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guarded_entrances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='manager',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'HouseManager'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_houses', to=settings.AUTH_USER_MODEL),
        ),
    ]
