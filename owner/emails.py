from django.core.mail import send_mail
from django.conf import settings
import random
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

# sending OTP function 
def send_OTP(email, username,template):
    user_email = [email]
    main_email = settings.EMAIL_HOST_USER

    # generating a random OTP
    OTP = random.randint(1000,9999)
    owner = get_user_model()
    # getting the user object
    owner = owner.objects.get(email=user_email[0])
    # storing their OTP
    owner.OTP = OTP
    owner.save()

    message = render_to_string(f'{template}',{'username':username, 'OTP':OTP})
    subject = 'email verfication'

    send_mail(subject=subject,message=message,recipient_list=user_email,from_email=main_email)










# t verfiy new email 
def verify_new(user,new_email):
    OTP = random.randint(1000,9999)
    user.OTP = OTP
    user.save()
    main_email = settings.EMAIL_HOST_USER
    message = render_to_string('OTP.html',{'username':user.username, 'OTP':OTP})
    subject = 'email verfication'
    send_mail(subject=subject,message=message,recipient_list=[new_email],from_email=main_email)
    return user

# ALERT !! this function is just for testing
def send_demo(validated_data):
    user_email = [validated_data['email']]
    user_name = validated_data['username']
    message = f'hi {user_name}, this is maintainance email to fix some bugs and add more security'
    subject = 'security update'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject=subject,message=message,recipient_list=user_email,from_email=email_from)