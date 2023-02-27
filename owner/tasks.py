from django.core.mail import send_mail
import datetime
import time
from django.conf import settings
import threading
from rest_framework.decorators import api_view 
from rest_framework.response import Response

def check_server():

    ceo = 'omermajdi250@gmail.com'
    message = 'hi this to assure you that the server is working'
    while True:
        send_mail(subject='server',message=message,recipient_list=[ceo],from_email=settings.EMAIL_HOST_USER)
        print('email was sent')
        time.sleep(1500)


# if __name__=="__main__":
#     check_server()

@api_view(['GET'])
def tasks_view(request):
    check_server()
    return Response({'task': 'started'})