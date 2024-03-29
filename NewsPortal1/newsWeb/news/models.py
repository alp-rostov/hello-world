from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    """ Table of categories

    - name
    - subscribers
    """
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, through='SubscribersUsers')  # manytomany relation to the table "User"

    def __str__(self):
        return f'{self.name}'


class SubscribersUsers(models.Model):
    """" Table for manytomany relation User and Category
    """
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)


class PostCategory(models.Model):
    """" Table for manytomany relation Post and Category """
    id_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comments(models.Model):
    """ Table of comments for the post

    - id_post
    - text
    - date
    - sum_rank
    - id_users
    """
    id_post = models.ForeignKey('Post', on_delete=models.CASCADE)  # onetomany relation to the table "Post"
    text = models.TextField()  # text comment
    date = models.DateTimeField(auto_now_add = True)  # date of the comment will be added
    sum_rank = models.IntegerField(default=0)  # rank of comment
    id_users = models.ForeignKey(User, on_delete=models.CASCADE)

POSITIONS = [('news', 'Новости'), ('article', 'Статьи')]

class Post(models.Model):
    """   Table for the posts:

    - head_article
    - text_post
    - date
    - type_post
    - sum_rank
    - id_author
    - category
    """
    head_article = models.CharField(max_length=255)  # post`s name
    text_post = models.TextField()  # text
    date = models.DateTimeField(auto_now_add = True)  # date of the post will be added
    type_post = models.CharField(max_length = 20, choices = POSITIONS, default = 'news')  # post`s type : news or article
    sum_rank = models.IntegerField(default = 0)
    id_author = models.ForeignKey('Author', on_delete = models.CASCADE)  # onetomany relation to the table "Author"
    category = models.ManyToManyField('Category', through = PostCategory)  # manytomany relation to the table "Category"

    def get_absolute_url(self):
        return reverse('news', args = [str(self.id)])


class Author(models.Model):
    """  Table for the author

    - full_name
    - e_mail
    - rank
    - id_users
    """
    full_name = models.CharField(max_length = 255)
    e_mail = models.EmailField(max_length = 150, null = True)
    rank = models.IntegerField(default = 0)
    id_users = models.OneToOneField(User, on_delete = models.DO_NOTHING)  # onetomany relation to the table "User"

    def update_rating(self):
        a = Post.objects.filter(id_author = self.id).aggregate(Sum('sum_rank'))['sum_rank__sum']*3
        b = Comments.objects.filter(id_users = self.id_users).aggregate(Sum('sum_rank'))['sum_rank__sum']
        c = Post.objects.filter(id_author = self.id).values('id')  # list (type dict) of the post`s 'id'
        d = 0
        for i in c:
            com = Comments.objects.filter(id_post = i['id']).aggregate(Sum('sum_rank'))['sum_rank__sum']
            if com:  # checking if the post has no comments
                d += com
        self.rank = a + b + d
        self.save()

    def __str__(self):
        return f'{self.full_name}'
