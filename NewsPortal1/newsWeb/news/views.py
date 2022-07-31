from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import news_filter

class NewsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'home.html'
    context_object_name = 'news'
    paginate_by = 2
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context

class NewsFilter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super ( ).get_queryset ( )
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filter = news_filter ( self.request.GET, queryset )
        # Возвращаем из функции отфильтрованный список товаров
        return self.filter.qs



    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['filter'] = news_filter
        return context


class News(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments']= context['new'].comments_set.all().values('text','id_users__username','date','sum_rank',)
        context['next'] = Post.objects.filter(id__gt=context['new'].id).order_by('id').values('id').first()
        context['prev'] = Post.objects.filter (id__lt=context['new'].id ).order_by('-id').values ( 'id' ).first()
        return context
