from django.core.mail import send_mail
import datetime
import time
from django.conf import settings
import threading

def check_server():
    ceo = 'omermajdi250@gmail.com'
    message = 'hi this to assure you that the server is working'
    while True:
        send_mail(subject='SERVER CHECK',message=message,recipient_list=[ceo],from_email=settings.EMAIL_HOST_USER)
        print('email was sent')
        time.sleep(1500)
