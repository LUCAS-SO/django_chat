Chat App con Django Channels

Proyecto de chat en tiempo real con Django y Channels, usando WebSockets para comunicación bidireccional.

🚀 Características

- Chat en tiempo real vía WebSocket.
- Grupo de chat único ("test").
- Capa de canales en memoria para - desarrollo.
- Interfaz sencilla con HTML y JavaScript.

🗂️ Estructura básica

core/
├─ asgi.py        Configuración ASGI y Channels
├─ settings.py    INSTALLED_APPS y CHANNEL_LAYERS
└─ urls.py        Rutas principales (admin/, chat/)

chat/
├─ consumers.py   Lógica de WebSocket
├─ routing.py     websocket_urlpatterns
├─ views.py       Vista del lobby
└─ templates/chat/
   └─ lobby.html   Interfaz y script JS