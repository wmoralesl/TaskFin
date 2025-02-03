import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Conectado al WebSocket"}))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "Mensaje vacío")
        await self.send(text_data=json.dumps({"message": f"Recibido: {message}"}))
