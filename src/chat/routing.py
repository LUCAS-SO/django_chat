from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    # usar path() es más claro:
    path('ws/socket-server/', ChatConsumer.as_asgi()),
]