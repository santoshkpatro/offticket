from django.contrib.auth.models import BaseUserManager
from accounts.utils import generate_user_id


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, user_id=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not user_id:
            user_id = generate_user_id()

        user = self.model(
            user_id=user_id,
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, user_id=None, password=None):
        """
        Creates and saves a superuser with the given email, full_name and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name,
            user_id=user_id
        )
        user.role = self.model.Roles.SUPERUSER
        user.save(using=self._db)
        return user