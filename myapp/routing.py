from django.urls import re_path
from .consumers import MiConsumer

websocket_urlpatterns = [
    re_path(r"ws/data/$", MiConsumer.as_asgi()),
]