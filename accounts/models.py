from typing import List
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from common.models import BaseUUIDModel
from accounts.utils import generate_user_id
from accounts.managers import UserManager
from organization.models import Organization


class User(BaseUUIDModel, AbstractBaseUser):
    """
    User Model
    """

    class Roles(models.TextChoices):
        """
        User Role
        """
        SUPERUSER = 'SU', 'Super User'
        CUSTOMER = 'CU', 'Customer'
        OWNER = 'OR', 'Owner'
        ORGANIZATION_ADMIN = 'OA', 'Organization Admin'
    

    organization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL,
        blank=True, null=True, related_name='users'
    )
    user_id = models.CharField(
        max_length=10, default=generate_user_id,
        verbose_name='User ID', unique=True
    )
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(
        max_length=20, blank=True, null=True
    )
    avatar = models.FileField(
        upload_to='avatars/', blank=True, null=True
    )
    role = models.CharField(
        max_length=2, choices=Roles.choices,
        verbose_name='User Role', default=Roles.CUSTOMER
    )
    is_email_verified = models.BooleanField(
        default=False,
        help_text="Check to verify user's email."
    )
    is_phone_verified = models.BooleanField(
        default=False,
        help_text="Check to verify user's phone number."
    )
    last_login = models.DateTimeField(
        blank=True, null=True
    )
    last_login_ip = models.GenericIPAddressField(
        blank=True, null=True
    )

    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS: List[str] = ['email', 'full_name']
    USERNAME_FIELD: str = 'user_id'

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
        unique_together = [
            'organization',
            'email'
        ]

    def __str__(self) -> str:
        return self.user_id

    """
    Django Admin Settings
    """

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.role == self.Roles.SUPERUSER


class Customer(User):
    """
    Customer Model
    """
    base_role = User.Roles.CUSTOMER

    class Meta:
        proxy = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
