from django.db import models
from django.contrib.auth.models import AbstractUser


class QuizAppUser(AbstractUser):
    is_moderator = models.BooleanField(default=False)  # superuser sets
    email = models.EmailField('email', unique=True, blank=False, null=False)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'QuizAppUser'
        verbose_name_plural = 'QuizAppUsers'

