# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from task.models import Task
from asgiref.sync import sync_to_async

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'tasks'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        if action == 'create_task':
            title = text_data_json.get('title')
            if title:
                # Crear la tarea en la base de datos
                task = await sync_to_async(Task.objects.create)(title=title)
                # Enviar la tarea creada a todos los clientes
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'task_created',
                        'task': {
                            'id': task.id,
                            'title': task.title,
                        },
                    },
                )

    async def task_created(self, event):
        # Enviar la tarea creada al cliente
        task = event['task']
        await self.send(text_data=json.dumps({
            'action': 'task_created',
            'task': task,
        }))