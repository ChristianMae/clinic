from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from utility.constants import OPTIONAL


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Staff(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    assigned_to = models.ForeignKey(
        'locations.Location',
        on_delete=models.CASCADE,
        related_name='staff_location',
        **OPTIONAL
    )
    middle_name = models.CharField(max_length=30, **OPTIONAL)
    age = models.CharField(max_length=3, **OPTIONAL)
    gender = models.CharField(max_length=6, **OPTIONAL)
    contact_no = models.CharField(max_length=11, **OPTIONAL)
    address = models.CharField(max_length=255, **OPTIONAL)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', )

    def __str__(self):
        return '{}, {} {}'.format(self.last_name, self.first_name, self.middle_name)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
