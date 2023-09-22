from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    # CharField should be used when you have a relatively short piece of text, like a name, title, or code,
    # and you want to limit the maximum length of the text.
    name = models.CharField(max_length=200)

    # TextField should be used when you expect to store a potentially large amount of text,
    # such as paragraphs of text, descriptions, or comments.
    description = models.TextField(null=True, blank=True)

    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    # auto now takes a snapshot on every time we save this item
    updated = models.DateTimeField(auto_now=True)

    # auto now add only takes a timestamp when we first save or create this instance
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # The - is used to sort it descending, by default it is sorted ascending
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]