# Generated by Django 3.2 on 2023-02-18 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_blog_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='subservices',
            options={'verbose_name': 'Sub_Service', 'verbose_name_plural': 'Sub_Services'},
        ),
    ]
