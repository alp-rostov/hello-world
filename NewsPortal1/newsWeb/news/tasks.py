import celery
from .models import User, Post
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создания объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст


@celery.shared_task
def send_mail_news(Create_news_: Post, id_categories_: list):

    emails = User.objects.filter(category__id__in=id_categories_).values('email').distinct()
    emails_list = [item['email'] for item in emails]  # mail list for sent mail
    html_content = render_to_string(
        'appointment_created.html',
        {
            'Create_news': Create_news_,
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'{Create_news_.head_article}',
        body=Create_news_.text_post,
        from_email='rostovclimb@mail.ru',
        to=emails_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
