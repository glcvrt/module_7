from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(verbose_name='Почта', unique=True)
    avatar = models.ImageField(upload_to='usersmedia/', verbose_name='Аватарка', **NULLABLE)
    phone = models.CharField(max_length=25, verbose_name='Номер телефона', **NULLABLE)
    username = models.CharField(max_length=150, verbose_name='Имя пользователя', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
