from django.db import models

from common.models import BaseUUIDModel
from theatres.models import Theatre
from screens.models import Screen
from shows.models import Show


class Slot(BaseUUIDModel):
    theatre = models.ForeignKey(
        Theatre, on_delete=models.CASCADE,
        related_name='theatre_slots'
    )
    screen = models.ForeignKey(
        Screen, on_delete=models.CASCADE,
        related_name='screen_slots'
    )
    show = models.ForeignKey(
        Show, on_delete=models.CASCADE,
        related_name='show_slots'
    )
    show_date = models.DateField()
    show_start_time = models.TimeField()
    show_end_time = models.TimeField(
        blank=True, null=True
    )
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'
        db_table = 'slots'

    def __str__(self) -> str:
        return str(self.id)