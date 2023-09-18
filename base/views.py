from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id': 1, 'name': "Let's Learn Python!"},
#     {'id': 2, 'name': "Design with me!"},
#     {'id': 3, 'name': "Backend developers!"},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, room_id):
    # return HttpResponse('Room')
    room = Room.objects.get(id=room_id)
    context = {'room': room}
    return render(request, 'base/room.html', context)
