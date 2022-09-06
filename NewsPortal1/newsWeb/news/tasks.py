from celery import shared_task
from .models import User, Post, Category, SubscribersUsers
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создания объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from datetime import date, timedelta


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

@shared_task
def week_news():
    """
    Function of sending news for the week
    Using in runapscheduler.py, celery.py
    """
    start = date.today() - timedelta(7)
    finish = date.today()
    categories = Category.objects.all()

    for category_ in categories:
        list_of_posts = Post.objects.filter(date__range=(start, finish), category=category_.pk)
        print(list_of_posts)
        subscribers_emails = []
        print(category_)
        for user_ in User.objects.all():
            user_mail = SubscribersUsers.objects.filter(id_category=category_.pk, id_user=user_.pk)
            if user_mail:
                subscribers_emails.append(user_.email)
        print(subscribers_emails)

        if list_of_posts:
            html_content = render_to_string('week_news.html', {'posts': list_of_posts, 'category': category_.name})
            # формируем тело письма
            msg = EmailMultiAlternatives(
                subject=f'Новости за неделю',
                from_email='rostovclimb@mail.ru',
                to=subscribers_emails,
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()  # отсылаем
