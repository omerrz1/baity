from django.core.mail import send_mail
from django.conf import settings
import random
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

import time




def send_check():
    attempt = 1
    while True:
        print('email sent ', attempt)
        ceo = 'omermajdi250@gmail.com'
        message = f'hi server is working this is attempt no {attempt}'
        time.sleep(60)
        send_mail(subject='SERVER CHECK',message=message,recipient_list=[ceo],from_email=settings.EMAIL_HOST_USER)
        attempt +=1



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





# ALERT !! this function is just for testing
def send_demo(validated_data):
    user_email = [validated_data['email']]
    user_name = validated_data['username']
    message = f'hi {user_name}, this is maintainance email to fix some bugs and add more security'
    subject = 'security update'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject=subject,message=message,recipient_list=user_email,from_email=email_from)