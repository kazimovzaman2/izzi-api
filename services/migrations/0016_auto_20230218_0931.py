# Generated by Django 3.2 on 2023-02-18 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0015_servicebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicebook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('address', models.CharField(max_length=100)),
                ('task_detail', models.TextField()),
                ('task_photo', models.ImageField(upload_to='order/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('new', 'New'), ('assigned', 'Assigned'), ('in_progress', 'In Progress'), ('finished', 'Finished'), ('cancelled', 'Cancelled')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='services.customer')),
                ('sub_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.subservice')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.tasker')),
            ],
        ),
    ]
