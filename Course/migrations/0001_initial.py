# Generated by Django 4.0.4 on 2022-05-03 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Instructor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coursename', models.CharField(max_length=100, unique=True)),
                ('period', models.CharField(blank=True, max_length=10, null=True)),
                ('display', models.BooleanField(default=True)),
                ('instructor', models.ManyToManyField(to='Instructor.instructor')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='username_course_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-create_at',),
                'abstract': False,
            },
        ),
    ]
