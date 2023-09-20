from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


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


def create_room(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def update_room(request, room_id):
    room = Room.objects.get(id=room_id)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/room_form.html', context)


def delete_room(request, room_id):
    room = Room.objects.get(id=room_id)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})
