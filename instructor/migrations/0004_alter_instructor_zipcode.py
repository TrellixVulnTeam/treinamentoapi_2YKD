# Generated by Django 4.0.4 on 2022-05-25 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zipcode', '0001_initial'),
        ('instructor', '0003_instructor_pkinstructor_name_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='zipcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='zips', to='zipcode.zipcode'),
        ),
    ]
