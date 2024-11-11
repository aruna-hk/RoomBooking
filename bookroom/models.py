from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
# Create your models here.

class Room(models.Model):
    room_purpose = [
        ('accomodation', 'accomodation'),
        ('meeting', 'meeting'),
        ('conference', 'conference'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room_name = models.CharField(max_length=30, null=False)
    room_available = models.BooleanField(default=True)
    room_price = models.FloatField()
    room_purpose = models.TextField(choices=room_purpose, default='accomodation')
    room_capacity = models.PositiveIntegerField()
    room_description = models.TextField()

    def __str__(self):
        return self.room_name

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    payable = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)
    paid_choices = [
        ('pending', 'pending'),
        ('paid', 'paid'),
    ]
    paid = models.TextField(choices=paid_choices, default='pending')

    def __str__(self):
        return "user {} booked room {} from {} to {}".format(self.user.username, self.room.room_name, self.check_in, self.check_out)

