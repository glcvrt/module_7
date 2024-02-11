from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import NULLABLE, Course, Lesson


class User(AbstractUser):
    email = models.EmailField(verbose_name='Почта')
    avatar = models.ImageField(upload_to='usersmedia/', verbose_name='Аватарка', **NULLABLE)
    phone = models.CharField(max_length=25, verbose_name='Номер телефона', **NULLABLE)
    username = models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Payments(models.Model):

    types_pay = [
        ('remittance', 'переводом на счет'),
        ('cash', 'наличными')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    date = models.DateTimeField(verbose_name='Дата оплаты', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment = models.IntegerField(verbose_name='сумма оплаты')
    payment_type = models.CharField(choices=types_pay, default='remittance', verbose_name='Способ оплаты'),

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
