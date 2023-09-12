from django.urls import path
from . import views 

urlpatterns =[
    path('', views.HomePage.as_view(),name='home-page'),
    path('docs/', views.docs.as_view(),name='home-page')
]