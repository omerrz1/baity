from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model

@receiver(pre_save, sender = get_user_model())
def user_check(instance , sender ):
    email = instance.email
    user=get_user_model().objects.filter(email=email,confirmed=True)
    if user:
        user.delete()
    else:
        print('user created without anything ')
