from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': "Let's Learn Python!"},
    {'id': 2, 'name': "Design with me!"},
    {'id': 3, 'name': "Backend developers!"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, room_id):
    # return HttpResponse('Room')
    room = None
    for i in rooms:
        if i['id'] == int(room_id):
            room = i

    context = {'room': room}
    return render(request, 'base/room.html', context)
