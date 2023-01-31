from django.core.mail import send_mail
from django.conf import settings

# sending OTP function 


# sending welcome email


# ALERT !! this function is just for testing 
def send_demo(validated_data):
    user_email = [validated_data['email']]
    user_name = validated_data['username']
    message = f'hi {user_name}, this is maintainance email to fix some bugs and add more security'
    subject = 'security update'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject=subject,message=message,recipient_list=user_email,from_email=email_from)