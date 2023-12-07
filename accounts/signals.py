# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from accounts.models import Accounts
# from customers.models import Customers


# @receiver(post_save, sender=Customers)
# def create_account(sender, instance, created, **kwargs):
#     if created:
#         Accounts.objects.create(user=instance)
