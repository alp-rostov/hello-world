from celery import shared_task
from .models import User, Post
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создания объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст


@shared_task
def send_mail_news(pk_, id_categories_):
    """"
    Mail sending function
    Using in views.py class Creat_n
    """
    post = Post.objects.get(id=pk_)
    emails = User.objects.filter(category__id__in=id_categories_).values('email').distinct()
    emails_list = [item['email'] for item in emails]  # mail list for sent mail
    html_content = render_to_string(
        'appointment_created.html',
        {
            'Create_news': post,
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'{post.head_article}',
        # body=Create_news_.,
        from_email='rostovclimb@mail.ru',
        to=emails_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
