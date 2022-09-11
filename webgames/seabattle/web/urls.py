from django.urls import path

from .views import Head, Shot

urlpatterns = [
    path('', Head.as_view(), name='head'),
    path('shot/', Shot, name='shot'),

]