import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    """
    class manager for providing a User(AbstractBaseUser) full control
    on this objects to create all types of User and this roles.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        pass data  to '_create_user' for creating normal_user .
        """
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        pass data to '_create_user' for creating super_user .
        """
        if email is None:
            raise TypeError("Users must have an email address.")
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True, primary_key=True)
    supplier_id = models.UUIDField(null=True, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    user_name = models.CharField(max_length=150, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def id_to_hex(self):
        return self.id.hex
