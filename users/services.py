import stripe


from config.settings import STRIPE_SECRET_KEY


stripe.api_key = STRIPE_SECRET_KEY


def create_product(payment):

    product = stripe.Product.create(
        name=payment.paid_course.name
    )
    return product['name']


def create_price(payment, product_name):

    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(payment.payment_amount)*100,
        product_data={"name": product_name},
    )

    return price['id']


def create_session(price_id):

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{
            'price': price_id,
            'quantity': 1
        }],
        mode='payment',

    )

    return session['url'], session['id']


def retrieve_session(session):
    """ Получаем детали сессии"""
    return stripe.checkout.Session.retrieve(session)
