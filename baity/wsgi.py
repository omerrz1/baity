"""
WSGI config for baity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from owner.tasks import check_server
import threading

from django.core.wsgi import get_wsgi_application



# a therad fro my mini server
threading.Thread(target=check_server).start()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baity.settings')

application = get_wsgi_application()
