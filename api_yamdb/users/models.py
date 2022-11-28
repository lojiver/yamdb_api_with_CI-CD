from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    USER_ROLES = (
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin'),
    )
    bio = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Биография'
    )

    role = models.CharField(
        max_length=30, choices=USER_ROLES, default=USER
    )
    email = models.EmailField(
        'Email', max_length=254, unique=True, null=False, blank=False
    )
    confirmation_code = models.TextField(
        max_length=99, null=True, blank=True,
        editable=False, unique=True
    )

    @property
    def is_admin(self):
        return (
            self.role == self.ADMIN
            or self.is_superuser
            or self.is_staff
        )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
