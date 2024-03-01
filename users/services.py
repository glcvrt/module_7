import stripe

from config import settings
from config.settings import STRIPE_SECRET_KEY

from users.models import Payments
from django.core.mail import send_mail


stripe.api_key = STRIPE_SECRET_KEY


def send_payment_link_to_mail(url, email):
    send_mail(
        subject='Оплата курса',
        message=f'Ссылка для оплаты курса: {url}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )


def get_session(serializer: Payments):
    """ Получает сессию для оплаты курса """
    course_title = serializer.course.title
    product = stripe.Product.create(name=course_title)
    price = stripe.Price.create(
        unit_amount=serializer.course.price * 100,
        currency='rub',
        product=product.id,
    )
    session = stripe.checkout.Session.create(
        success_url='https://example.com/success',
        line_items=[
            {
                'price': price.id,
                'quantity': 1,
            }
        ],
        mode='payment',
        customer_email=serializer.user.email
    )
    send_payment_link_to_mail(session.url, serializer.user.email)
    return session


def retrieve_session(session):
    """ Получаем детали сессии"""
    return stripe.checkout.Session.retrieve(session)
