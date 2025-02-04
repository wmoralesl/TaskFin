from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Task
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Unirse al grupo 'tasks_group'
        await self.channel_layer.group_add('tasks_group', self.channel_name)

        # Enviar los registros existentes al cliente
        tasks = await self.get_tasks()
        await self.send(text_data=json.dumps({
            'type': 'initial_data',
            'tasks': tasks,
        }))

    async def disconnect(self, close_code):
        # Salir del grupo 'tasks_group'
        await self.channel_layer.group_discard('tasks_group', self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']

        if action == 'create_task':
            title = text_data_json['title']
            task = await self.create_task(title)

            # Notificar a todos los clientes sobre la nueva tarea
            await self.channel_layer.group_send(
                'tasks_group',  # Nombre del grupo
                {
                    'type': 'task_created',
                    'task': {'id': task.id, 'title': task.title},
                }
            )

    async def task_created(self, event):
        # Enviar la nueva tarea al cliente
        await self.send(text_data=json.dumps({
            'type': 'task_created',
            'task': event['task'],
        }))

    @database_sync_to_async
    def get_tasks(self):
        tasks = Task.objects.all()
        return [{'id': task.id, 'title': task.title} for task in tasks]

    @database_sync_to_async
    def create_task(self, title):
        return Task.objects.create(title=title)