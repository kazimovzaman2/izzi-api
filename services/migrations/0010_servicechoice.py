# Generated by Django 3.2 on 2023-02-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_delete_servicechoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_service', models.IntegerField(choices=[(1, 'Car Repair'), (2, 'Home Reapir'), (3, 'Baby walking'), (4, 'Baby siting')])),
            ],
        ),
    ]
