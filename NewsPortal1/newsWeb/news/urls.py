from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, News, NewsFilter, Create_n, Create_edit, Delete_news


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path ('', NewsList.as_view ( ), name='home' ),
   path ( '<int:pk>', News.as_view(), name='news'),
   path ( 'search', NewsFilter.as_view ( ), name='search' ),
   path ( 'create', Create_n.as_view(), name='create_news'),
   path ( 'article/', Create_n.as_view(), name='create_article'),
   path('<int:pk>/update/', Create_edit.as_view(), name='edit'),
   path ( '<int:pk>/delete/', Delete_news.as_view ( ), name='delete' ),
]