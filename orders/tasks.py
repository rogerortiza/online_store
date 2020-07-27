from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order ir
    successfully created.
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n ' \
              f'You have successfully placed an order. ' \
              f'Your order id is {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@myshop.com',
                          [order.email])
    return mail_sent
