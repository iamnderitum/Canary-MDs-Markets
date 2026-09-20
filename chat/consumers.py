import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from chat.models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.id = self.scope["url_route"]["kwargs"]["course_id"]
        self.room_group_name = f"chat_{self.id}"

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        # accept connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data = None, bytes_data = None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        now = timezone.now()
        # send message to room group
        # self.send(text_data=json.dumps({"message": message}))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": self.user.username,
                "datetime": now.isoformat(),
            }
        )
        # persist message
        await self.persist_message(message)

    # receive message from group
    async def chat_message(self, event):
        # send message to websocket
        await self.send(text_data=json.dumps(event))

    async def persist_message(self, message):
        # send message to WebSocket
        await Message.objects.acreate(
            user=self.user, course_id=self.id, content=message
        )