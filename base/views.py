from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Room, Topic, User, Message
from .forms import RoomForm


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except():
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    page = 'register'
    form = UserCreationForm()
    context = {
        'page': page,
        'form': form,
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration. Please try again!')

    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    # __icontains means that it is case-sensitive, and it contains the topic contains q
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_activities = Message.objects.all()

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
        'room_activities': room_activities,
    }

    return render(request, 'base/home.html', context)


def room(request, room_id):
    room = Room.objects.get(id=room_id)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', room_id)

    # Query for a specific child of room
    # Do not use the variable messages since it will be displayed as an error by the flash images

    context = {
        'room': room,
        'room_messages': room_messages,
        'participants': participants,
    }
    return render(request, 'base/room.html', context)


@login_required(login_url='/login')
def create_room(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='/login')
def update_room(request, room_id):
    room = Room.objects.get(id=room_id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You're not allowed here!")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/room_form.html', context)


@login_required(login_url='/login')
def delete_room(request, room_id):
    room = Room.objects.get(id=room_id)

    if request.user != room.host:
        return HttpResponse("You're not allowed here!")

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='/login')
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)

    if request.user != message.user:
        return HttpResponse("You're not allowed here!")

    if request.method == 'POST':
        message.delete()
        next_url = request.POST.get('next')

        # Redirect to the 'next' URL
        return HttpResponseRedirect(next_url)

    return render(request, 'base/delete.html', {'obj': message})
