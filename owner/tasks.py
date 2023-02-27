from django.contrib.auth import get_user_model
import datetime
import time
import threading
from .emails import send_OTP



def check():
    while True:
        send_OTP('omermajdi250@gmail.com',' CEO ','serverworking.html')
        time.sleep(3000)



if __name__=="__main__":
    check()
