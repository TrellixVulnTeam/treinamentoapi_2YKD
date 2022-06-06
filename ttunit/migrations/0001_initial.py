# Generated by Django 4.0.4 on 2022-06-05 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ttcompany', '0002_rename_codeare_ttcompany_codearea'),
    ]

    operations = [
        migrations.CreateModel(
            name='TTUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Atalho')),
                ('unittype', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('R', 'Rented'), ('S', 'Sold'), ('A', 'Available')], default='A', max_length=8)),
                ('active', models.BooleanField(default=False)),
                ('businessdate', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('modal', models.CharField(choices=[('R', 'Rent'), ('S', 'Sell')], default='R', max_length=8)),
                ('bedroom', models.IntegerField(blank=True, null=True)),
                ('restrooom', models.IntegerField(blank=True, null=True)),
                ('petpolicy', models.CharField(blank=True, max_length=20, null=True)),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ttcompany.ttcompany')),
            ],
            options={
                'ordering': ('-create_at',),
                'abstract': False,
            },
        ),
    ]