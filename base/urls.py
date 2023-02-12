from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('hotel/', views.hotel, name="home"),
    path('hotelroom/<str:pk>/',views.hotelroom, name = 'hotelroom'),
]