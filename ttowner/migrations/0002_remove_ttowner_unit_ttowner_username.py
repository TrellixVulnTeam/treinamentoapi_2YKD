# Generated by Django 4.0.4 on 2022-06-07 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ttowner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ttowner',
            name='unit',
        ),
        migrations.AddField(
            model_name='ttowner',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='username_ttowner', to=settings.AUTH_USER_MODEL),
        ),
    ]
