
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

path ( '', HomePageView.as_view ( ), name='home' ),
