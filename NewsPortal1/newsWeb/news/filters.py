from django_filters import FilterSet, CharFilter, DateTimeFilter, ModelChoiceFilter, DateFromToRangeFilter,
from .models import Post, Author

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

    date = DateFromToRangeFilter (
        field_name='date'
    )


    class Meta:
        model = Post
        fields = ['h_arcticle', 'author']
