from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # Use all the fields
        # fields = '__all__'
        fields = ['name', 'description', 'topic']
