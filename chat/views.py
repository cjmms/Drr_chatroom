# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.http import HttpResponse
from .models import Room

def index(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'chat/index.html', context)
    #return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


