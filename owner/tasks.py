from .emails import send_check
from rest_framework.decorators import api_view
from rest_framework.response import Response

import threading

@api_view(['GET'])
def task_view (request):
    threading.Thread(target=send_check).start()
    return Response({'taske': 'done'})