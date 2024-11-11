from django.forms import ModelForm
from .models import Room, Booking

class RoomBookFilterModel(ModelForm):
    class Meta:
        model = Room

        fields = ['room_purpose',]

class BookRoomForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'room', 'check_in', 'check_out']

