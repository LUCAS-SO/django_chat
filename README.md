Chat App con Django Channels

Proyecto de chat en tiempo real con Django y Channels, usando WebSockets para comunicación bidireccional.

🚀 Características

- Chat en tiempo real vía WebSocket.
- Grupo de chat único ("test").
- Capa de canales en memoria para - desarrollo.
- Interfaz sencilla con HTML y JavaScript.

🗂️ Estructura básica

core/</br>
├─ asgi.py        Configuración ASGI y Channels</br>
├─ settings.py    INSTALLED_APPS y CHANNEL_LAYERS</br>
└─ urls.py        Rutas principales (admin/, chat/)</br>

chat/</br>
├─ consumers.py   Lógica de WebSocket</br>
├─ routing.py     websocket_urlpatterns</br>
├─ views.py       Vista del lobby</br>
└─ templates/chat/</br>
   └─ lobby.html   Interfaz y script JS
