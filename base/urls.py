from . import views
from django.urls import path



urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('/update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('/creat-room/', views.creatRoom, name="creat-room"),
]