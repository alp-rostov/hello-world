from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .filters import news_filter
from .forms import Create_news
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, request

class NewsList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'home.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()

        context = super ( ).get_context_data ( **kwargs )
        context['get_author'] = not self.request.user.groups.filter ( name='author' ).exists ( )

        return context


class NewsFilter(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = '-date'

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

class Create_n(PermissionRequiredMixin, CreateView):
    # Указываем нашу разработанную форму
    form_class = Create_news
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'create.html'
    permission_required = ('news.add_post',)


    def form_valid(self, form):
        b= self.request.POST['category'][0]
        Create_news = form.save ( commit=False )
        if self.request.path=='/home/news/create':
            Create_news.type_post = 'news'
        else:
            Create_news.type_post = 'article'
        Create_news.save()

        post1 = Create_news # add category
        cat1 = Category.objects.get ( pk=b)
        post1.category.add ( cat1 )

        return HttpResponseRedirect('/home/')

class Create_edit(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    # Указываем нашу разработанную форму
    form_class = Create_news
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'create.html'
    permission_required = ('news.change_post',)

class Delete_news(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')