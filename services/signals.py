from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Tasker, Customer


@receiver(post_save, sender=User)
def create_related_model(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'tasker':
            Tasker.objects.create(user=instance)
        elif instance.user_type == 'customer':
            Customer.objects.create(user=instance)
    else:
        if instance.user_type == 'tasker':
            try:
                customer = instance.customer
                customer.delete()
            except Customer.DoesNotExist:
                pass
            try:
                tasker = instance.tasker
            except Tasker.DoesNotExist:
                Tasker.objects.create(user=instance)
        elif instance.user_type == 'customer':
            try:
                tasker = instance.tasker
                tasker.delete()
            except Tasker.DoesNotExist:
                pass
            try:
                customer = instance.customer
            except Customer.DoesNotExist:
                Customer.objects.create(user=instance)
