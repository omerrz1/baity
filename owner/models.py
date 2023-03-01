from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model

class ownerManager(BaseUserManager):
    def create_user(self, username, email, password,phone):
        if not email:
            raise ValueError('please provide an email ! ')
        if not username:
            raise ValueError('')

        user = self.model(email=self.normalize_email(email.lower()))
        user.username = username
        user.phone = phone
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,phone, username, password):
        user = self.create_user(
            email=email,phone=phone, username=username, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create(self, username, password,phone, email):
        user = self.create_user(
            email=email, username=username, phone= phone,password=password)
        user.save(using=self._db)
        return user

# user model


class Owner (AbstractBaseUser):
    username = models.CharField(max_length=60)
    email = models.EmailField(verbose_name='email', unique=True)
    phone = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    OTP = models.IntegerField(default=0)

    REQUIRED_FIELDS = ['username','phone']
    USERNAME_FIELD = 'email'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username

    objects = ownerManager()


# signals 

@receiver(pre_save, sender = get_user_model())
def user_check(instance , sender ):
    email = instance.email
    user=get_user_model().objects.filter(email=email,confirmed=True)
    if user:
        user.delete()
    else:
        print('user created without anything ')
