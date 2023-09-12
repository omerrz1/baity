from django.shortcuts import render
from .predict import predictEmotion
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def emotionView(request,*args,**kwargs):
    text = request.data[text]
    emotion = predictEmotion(text)
    return Response({'emotion':emotion})

