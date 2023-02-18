# Generated by Django 3.2 on 2023-02-17 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='TaskerCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='tasker_certificate/')),
            ],
            options={
                'verbose_name': 'Tasker Certificate',
                'verbose_name_plural': 'Tasker Certificates',
            },
        ),
        migrations.CreateModel(
            name='TaskerSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=10)),
            ],
            options={
                'verbose_name': 'Tasker Skill',
                'verbose_name_plural': 'Tasker Skills',
            },
        ),
        migrations.CreateModel(
            name='Tasker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('tasks_done', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('certificate', models.ManyToManyField(blank=True, to='services.TaskerCertificate')),
                ('skills', models.ManyToManyField(blank=True, to='services.TaskerSkills')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_cities', models.ManyToManyField(blank=True, to='services.City')),
            ],
            options={
                'verbose_name': 'Tasker',
                'verbose_name_plural': 'Taskers',
            },
        ),
    ]