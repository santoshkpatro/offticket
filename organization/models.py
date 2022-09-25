from django.db import models
from common.models import BaseUUIDModel


class Organization(BaseUUIDModel):
    """
    Organization Model
    """
    
    org_username = models.CharField(
        max_length=100,
        unique=True
    )

    org_name = models.CharField(max_length=200)
    org_description = models.TextField(blank=True, null=True)
    org_logo = models.FileField(
        blank=True,
        null=True,
        upload_to='organizations/logo'
    )

    is_org_verified = models.BooleanField(default=False)
    is_org_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        db_table = 'organizations'

    def __str__(self) -> str:
        return self.org_username
