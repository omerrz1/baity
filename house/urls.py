from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainHouses.as_view(), name='main-house-list'),
    path('create/', views.CreateHouse.as_view(), name='create-house'),
    path('photos/', views.CreatePhotos.as_view(), name='create-photos'),
    path('mine/', views.Myhouses.as_view(), name = 'my-house'),
    path('<int:pk>/',views.HouseDetails.as_view(), name = 'houes-details'),
    path('update/<int:pk>/',views.UpdateHouse.as_view(),name= 'update-house'),
    path('delete/<int:pk>/',views.DeleteHouse.as_view(), name = 'delete-houe'),
    path('search/', views.SearchHouse.as_view(), name = 'searc-house')


]
