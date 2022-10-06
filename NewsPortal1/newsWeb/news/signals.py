from django.db.models.signals import post_save
from django.template.loader import render_to_string
from .models import Post, Category, User, SubscribersUsers
from django.dispatch import receiver
from datetime import date, timedelta
from django.core.mail import EmailMultiAlternatives, mail_managers
import logging

@receiver(post_save, sender=Post)  # создаём функцию-обработчик с параметрами под регистрацию сигнала
def notify_managers_news(sender, instance, created, **kwargs):

    """  the function of sending news when adding news  """
    if created:
        subject = f'Добавлена новость: {instance.head_article} от {instance.date.strftime ( "%d %m %Y" )}'

    # else:
    #     subject = f'Изменения в новости: {instance.head_article} от {instance.date.strftime ( "%d %m %Y" )}'

        try:
            mail_managers (
                subject=subject,
                message=f'{instance.head_article} http://127.0.0.1:8000/home/{instance.id}  '
            )

        except Exception:
            print("ошибка отправки сообщения на почту")
            # logging.Logger.error ( "error - can`t sent email" )