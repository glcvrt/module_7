from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from materials.models import NULLABLE, Course, Lesson


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    email = models.EmailField(verbose_name='Почта')
    avatar = models.ImageField(upload_to='usersmedia/', verbose_name='Аватарка', **NULLABLE)
    phone = models.CharField(max_length=25, verbose_name='Номер телефона', **NULLABLE)
    username = models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Роль')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Дата последнего входа', **NULLABLE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Payments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    date = models.DateTimeField(verbose_name='Дата оплаты', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=1, choices=[('1', 'Наличные'), ('2', 'Безнал')],
                                      verbose_name='Метод платежа',)
    is_successful = models.BooleanField(default=False, verbose_name='Статус платежа')
    session = models.CharField(max_length=150, verbose_name='Сессия для оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
