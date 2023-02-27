from django.contrib.auth import get_user_model
import datetime
import time
import threading
from emails import send_OTP


user = get_user_model().all()
def check():
    while True:
        for owner in user:
            print (owner)
        time.sleep(3000)



if __name__=="__main__":
    check()
