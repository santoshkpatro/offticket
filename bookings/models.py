from django.db import models

from common.models import BaseUUIDModel
from accounts.models import User
from theatres.models import Theatre
from screens.models import Screen, Seat
from shows.models import Show
from slots.models import Slot


class Booking(BaseUUIDModel):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name='user_bookings'
    )
    theatre = models.ForeignKey(
        Theatre, on_delete=models.SET_NULL,
        null=True, related_name='theatre_bookings'
    )
    screen = models.ForeignKey(
        Screen, on_delete=models.SET_NULL,
        null=True, related_name='screen_bookings'
    )
    show = models.ForeignKey(
        Show, on_delete=models.SET_NULL,
        null=True, related_name='show_bookings'
    )
    seat = models.ForeignKey(
        Seat, on_delete=models.SET_NULL,
        null=True, related_name='seat_bookings'
    )
    slot = models.ForeignKey(
        Slot, on_delete=models.SET_NULL,
        null=True, related_name='slot_bookings'
    )
    seat_no = models.CharField(
        max_length=5,
        blank=True, null=True
    )
