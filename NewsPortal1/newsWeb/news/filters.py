import requests
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author, Category
from django import forms

class news_filter(FilterSet):
    h_arcticle = CharFilter (
        field_name='head_article',
        label='Название статьи',
        lookup_expr='icontains'
    )

    author = ModelChoiceFilter (
        field_name='id_author__full_name',
        label='Автор',
        queryset=Author.objects.order_by('full_name').all(),
        lookup_expr='icontains',
    )

    category = ModelChoiceFilter (
        field_name='category__name',
        label='Категория',
        queryset=Category.objects.order_by ( 'name' ).all ( ),
        lookup_expr='icontains',
    )

    date = DateFilter ( field_name="date",
                        widget=forms.DateInput(attrs={'type': 'date'}),
                        label='Дата',
                        lookup_expr='gte',
                     )

    class Meta:
        model = Post
        fields = ['h_arcticle', 'author', 'date']
