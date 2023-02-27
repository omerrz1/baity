from django.contrib.auth import get_user_model
import datetime
import time
import threading
from emails import send_OTP
import django
django.setup()

user = get_user_model().all()
ceo = 'omermajdi250@gmail.com'
ceo_template = 'serverworking.html'
def check():
    while True:
        send_OTP(email=ceo,username=' CEO ', template=ceo_template)
        time.sleep(1500)



if __name__=="__main__":
    check()
