import json
from channels .generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        print("🔔 Conexión aceptada, canal añadido al grupo", self.room_group_name)

    def receive(self, text_data):
        print("🔹 receive() raw:", text_data)
        data = json.loads(text_data)
        message = data.get('message')
        if not message:
            print("⚠️ receive(): mensaje vacío, ignoro")
            return

        print("🔹 receive(): reenviando al grupo:", message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        print("🔹 receive(): group_send hecho")

    def chat_message(self, event):
        message = event['message']
        print("🔸 chat_message(): enviando al cliente:", message)
        self.send(text_data=json.dumps({
            'type': 'chat',        # <-- ojo aquí
            'message': message
        }))
# https://channels.readthedocs.io/en/stable/topics/channel_layers.html#in-memory-channel-layer

