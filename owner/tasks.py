import django
django.setup()
from django.conf import settings
settings.configure()
from django.core.mail import send_mail
import datetime
import time
import threading
from emails import send_OTP


ceo = 'omermajdi250@gmail.com'
message = 'hi this to assure you that the server is working'
def check():
    while True:
        send_mail(subject='server check',message=message,recipient_list=[ceo],from_email=settings.EMAIL_HOST_USER)
        time.sleep(1500)



if __name__=="__main__":
    check()
