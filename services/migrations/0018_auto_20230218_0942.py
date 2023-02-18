# Generated by Django 3.2 on 2023-02-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_alter_servicebook_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicebook',
            options={'verbose_name': 'Service Book', 'verbose_name_plural': 'Service Books'},
        ),
        migrations.RemoveField(
            model_name='servicebook',
            name='taskers',
        ),
        migrations.AlterField(
            model_name='servicebook',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
