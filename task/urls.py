from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tareas')
urlpatterns = [
    path('', include(router.urls)),
]
