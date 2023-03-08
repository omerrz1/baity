from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateOwner.as_view(), name='create-owner'),
    path('update/up/<int:id>/', views.UpdateOwner_username_phone.as_view(), name='update-username-phone'),
    path('update/email/<int:id>/', views.UpdateOwner_email.as_view(), name='updatae-email'),
    path('delete/<str:email>/', views.DeleteOwner.as_view(), name='delete-owner'),
    path('detail/<str:username>/',
         views.ownerDetail.as_view(), name='owner-details'),
    path('update_password/', views.Update_password , name = 'pdate-password')
    path('deleteme/', views.delete_me , name = 'delete my account'),
    path('verify/', views.verify_OTP, name='verify-OTP'),
    path('', views.ownersList.as_view(), name='owners'),
    path('verify-email/',views.verfiy_email, name='email-otp'),
    path('profile/',views.MyProfile.as_view(), name="my-profile")
]
