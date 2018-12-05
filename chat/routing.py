# chat/routing.py
from django.urls import path
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    #path('ws/<str:room_name>/', consumers.ChatConsumer),
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
