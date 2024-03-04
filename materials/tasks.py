import datetime

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from materials.models import Course
from users.models import User


@shared_task
def check_update():
    for i in Course.objects.all():
        if i.date_update > i.date_preview:
            send_mail(
                subject='Информация о курсе',
                message=f'Курс был обновлен',
                from_email=settings.EMAIL_HOST_USER
            )
            i.date_preview = i.date_update
            i.save()


@shared_task
def check_login():
    a = timezone.now()
    for i in User.objects.all():
        count_date = a - i.last_login.replace(tzinfo=timezone.utc)
        if count_date > datetime.timedelta(days=30):
            i.role = 'member'
            i.save()
