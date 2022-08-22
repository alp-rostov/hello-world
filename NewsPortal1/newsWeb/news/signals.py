import requests
from django.db.models.signals import post_save
from django.core.mail import mail_managers
from .models import Post
from django.dispatch import receiver
from datetime import datetime


# создаём функцию-обработчик с параметрами под регистрацию сигнала
@receiver(post_save, sender=Post)
def notify_managers_news(sender, instance, created, **kwargs):
    if created:
        subject = f'Добавлена новость: {instance.head_article} от {instance.date.strftime ( "%d %m %Y" )}'
    else:
        subject = f'Изменения в новости: {instance.head_article} от {instance.date.strftime ( "%d %m %Y" )}'

    mail_managers (
        subject=subject,
        message=instance.text_post,
    )



