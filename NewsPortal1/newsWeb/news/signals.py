import requests
from django.db.models.signals import post_save
from django.core.mail import mail_managers
from .models import Post, Category, User, SubscribersUsers
from django.dispatch import receiver
from datetime import date, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# создаём функцию-обработчик с параметрами под регистрацию сигнала
@receiver(post_save, sender=Post)
def notify_managers_news(sender, instance, created, **kwargs):
    if created:
        subject = f'Добавлена новость: {instance.head_article} от {instance.date.strftime ( "%d %m %Y" )}'
    else:
        subject = f'Изменения в новости: {instance.head_article} от {instance.date.strftime ( "%d %m %Y" )}'

    mail_managers (
        subject=subject,
        message=f'{ instance.head_article } "http://127.0.0.1:8000/home/{ instance.id }"подробнее...'
    )


def week_news():

    start = date.today ( ) - timedelta (7)
    finish = date.today ( )

    categories = Category.objects.all()

    for category_ in categories:
        list_of_posts = Post.objects.filter ( date__range=(start, finish), category=category_.pk )
        print(list_of_posts)
        # создадим список, куда будем собирать почтовые адреса подписчиков
        subscribers_emails = []
        print(category_)
        for user_ in User.objects.all ( ):
            user_mail=SubscribersUsers.objects.filter(id_category=category_.pk, id_user=user_.pk)
            if user_mail:
                subscribers_emails.append ( user_.email )
        print(subscribers_emails)

        if list_of_posts:
            html_content = render_to_string ( 'week_news.html',
                                              {'posts': list_of_posts, 'category': category_.name} )
            # формируем тело письма
            msg = EmailMultiAlternatives (
                subject=f'Новости за неделю',
                from_email='rostovclimb@mail.ru',
                to=subscribers_emails,
            )
            msg.attach_alternative ( html_content, "text/html" )
            msg.send ( )  # отсылаем
