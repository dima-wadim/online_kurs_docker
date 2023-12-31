from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', null=True, blank=True)
    phone = models.CharField(max_length=50, verbose_name='Номер телефона', null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name='Город', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




