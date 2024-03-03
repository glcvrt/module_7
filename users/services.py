import stripe

from config import settings
from config.settings import STRIPE_SECRET_KEY

from users.models import Payments
from django.core.mail import send_mail


stripe.api_key = STRIPE_SECRET_KEY


def create_price(payment):

    product = stripe.Product.create(
        name=payment.paid_course.name
    )

    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(payment.payment_amount)*100,
        product_data={"name": product['name']},
    )

    return price['id']


def create_session(stripe_price_id):

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{
            'price': stripe_price_id,
            'quantity': 1
        }],
        mode='payment',

    )

    return session['url'], session['id']


def retrieve_session(session):
    """ Получаем детали сессии"""
    return stripe.checkout.Session.retrieve(session)
