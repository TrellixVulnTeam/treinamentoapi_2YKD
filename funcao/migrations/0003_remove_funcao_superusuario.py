# Generated by Django 4.0.4 on 2022-04-30 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcao', '0002_alter_funcao_superusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcao',
            name='superusuario',
        ),
    ]
