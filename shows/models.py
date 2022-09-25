from django.db import models
from django.contrib.postgres.fields import ArrayField

from common.models import BaseUUIDModel
from theatres.models import Theatre
from screens.models import Screen


class Show(BaseUUIDModel):
    theatre = models.ForeignKey(
        Theatre, on_delete=models.CASCADE,
        related_name='theatre_shows'
    )
    screen = models.ForeignKey(
        Screen, on_delete=models.CASCADE,
        related_name='screen_shows'
    )
    thumbnail = models.FileField(
        upload_to='shows/thumbnails', 
        blank=True, null=True
    )
    title = models.CharField(max_length=300)
    description = models.TextField(
        blank=True, null=True
    )
    languages = ArrayField(
        base_field=models.CharField(max_length=20),
        blank=True, null=True
    )
    genre = ArrayField(
        base_field=models.CharField(max_length=20),
        blank=True, null=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Show'
        verbose_name_plural = 'Shows'
        db_table = 'shows'

    def __str__(self) -> str:
        return self.title
