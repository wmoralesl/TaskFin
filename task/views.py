from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(is_active=True)
    serializer_class = TaskSerializer