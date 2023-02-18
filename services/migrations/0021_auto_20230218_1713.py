# Generated by Django 3.2 on 2023-02-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default='images/default_blog.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='task_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='thumbnail',
            field=models.ImageField(default='images/default_service.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='servicebook',
            name='attachment',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='thumbnail',
            field=models.ImageField(default='images/default_service.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='taskercertificate',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
