from django.urls import path
from . import views , tasks

urlpatterns = [
    path('create/', views.CreateOwner.as_view(), name='create-owner'),
    path('update/up/<int:id>/', views.UpdateOwner_username_phone.as_view(), name='update-username-phone'),
    path('update/email/<int:id>/', views.UpdateOwner_email.as_view(), name='updatae-email'),
    path('delete/<str:username>/', views.DeleteOwner.as_view(), name='dlete-owner'),
    path('detail/<str:username>/',
         views.ownerDetail.as_view(), name='owner-details'),
    path('verify/', views.verify_OTP, name='verify-OTP'),
    path('', views.ownersList.as_view(), name='owners'),
    path('verify-email/',views.verfiy_email, name='email-otp'),
    path('run/', tasks.task_view , name='taske'),
    path('profile/',views.MyProfile.as_view(), name="my-profile")
]
