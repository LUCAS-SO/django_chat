from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.lobby, name='lobby'),
    #path('chat/<str:room_name>/', views.room, name='room'),
]