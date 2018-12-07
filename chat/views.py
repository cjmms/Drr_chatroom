# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.http import HttpResponse
from .models import Room

def index(request):
    print("index!!!")
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'chat/index.html', context)
    #return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def create_room(request):
    if request.method == "POST":
        name = request.POST.get('room_name')
        new_room = Room(room_text=name)
        hasSame = 0

        for room in Room.objects.all():
            if room.room_text == new_room.room_text: hasSame = 1

        if hasSame == 0:
            Room.objects.create(room_text=name)
        room_list = Room.objects.all()

        context = {'room_list': room_list}
        return render(request, 'chat/index.html', context)


