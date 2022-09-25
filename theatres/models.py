from django.db import models

from common.models import BaseUUIDModel
from organization.models import Organization


class Theatre(BaseUUIDModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE,
        related_name='theatres'
    )
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    is_open = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Theatre'
        verbose_name_plural = 'Theatres'
        db_table = 'theatres'

    def __str__(self) -> str:
        return self.name