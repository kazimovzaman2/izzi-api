# Generated by Django 3.2 on 2023-02-18 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_servicechoice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceChoice',
            new_name='ServiceBook',
        ),
    ]
