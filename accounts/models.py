# accounts/models.py

from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    email = models.EmailField(
    null=True,
    blank=True
)

    phone = models.CharField(
        max_length=15
    )

    subject = models.CharField(
        max_length=100
    )

    role = models.CharField(
        max_length=50,
        default='Teacher'
    )

    is_registered = models.BooleanField(
        default=False
    )

    def __str__(self):

        return self.email