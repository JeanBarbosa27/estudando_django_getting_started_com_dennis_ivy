from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from accounts.models import Customer

@receiver(post_save, sender=User)
def create_customer_profile(sender, created, instance, **kwargs):
    if created:
        group = Group.objects.get(name="customer")
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )
        print(f"Profile created for {instance.username}")
