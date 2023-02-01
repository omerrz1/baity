from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateOwner.as_view(), name='create-owner'),
    path('update/<str:username>/', views.UpdateOwner.as_view(), name='update-owner'),
    path('delete/<str:username>/', views.DeleteOwner.as_view(), name='dlete-owner'),
    path('detail/<str:username>/',
         views.ownerDetail.as_view(), name='owner-details'),
    path('verify/', views.OTPVerfiy.as_view(), name='verify_OTP'),
    path('', views.ownersList.as_view(), name='owners'),
]
