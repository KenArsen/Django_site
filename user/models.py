from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name='Аватар',
        blank=True,
        null=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата рождение",
    )

    def __str__(self):
        return self.email
