from django.db import models

from common.models import BaseUUIDModel
from theatres.models import Theatre


class Screen(BaseUUIDModel):
    theatre = models.ForeignKey(
        Theatre, on_delete=models.CASCADE,
        related_name='screens'
    )
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Screen'
        verbose_name_plural = 'Screens'
        db_table = 'screens'

    def __str__(self) -> str:
        return self.name


class Seat(BaseUUIDModel):
    screen = models.ForeignKey(
        Screen, on_delete=models.CASCADE,
        related_name='seats'
    )
    seat_no = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Seat'
        verbose_name_plural = 'Seats'
        db_table = 'seats'

    def __str__(self) -> str:
        return self.seat_no