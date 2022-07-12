from django.db import models

class Category(models.Model): #Table of categories
    name=models.CharField(max_length=255, unique=True)

class Users(models.Model):
    pass

class PostCategory(models.Model): #Table for manytomany relation Post and Category
    id_post=models.ForeignKey('Post', on_delete=models.CASCADE)
    id_caregory=models.ForeignKey('Category', on_delete=models.CASCADE)

class Comments(models.Model): #Table of comments for the post
    id_post=models.ForeignKey('Post', on_delete=models.CASCADE) # onetomany relation to the table "Post"
    text=models.TextField() # text comment
    date=models.DateTimeField(auto_now_add = True) #date of the comment will be added
    sum_rank=models.IntegerField(default=0) #rank of comment
    count_rank=models.IntegerField(default=0) #count of vote
    id_users=models.ForeignKey('Users', on_delete=models.CASCADE) # onetomany relation to the table "Users"

POSITIONS = [('news', 'Новости'), ('article', 'Статьи')]
class Post(models.Model): #Table for the posts
    head_article=models.CharField(max_length=2550) #post`s name
    text_post=models.TextField() #text
    date=models.DateTimeField(auto_now_add = True) #date of the post will be added
    type_post=models.CharField(max_length = 50, choices = POSITIONS, default = 'news') #post`s type : news or article
    sum_rank = models.IntegerField (default=0)
    count_rank = models.IntegerField (default=0)
    id_author=models.ForeignKey('Author', on_delete=models.CASCADE) # onetomany relation to the table "Author"
    id_category=models.ManyToManyField('Category', through=PostCategory) #manytomany relation to the table "Category"

class Author(models.Model): #Table for the author
    full_name=models.CharField(max_length=255)
    e_mail=models.EmailField(max_length=150, null=True)
    rank=models.IntegerField(default=0)
    id_users=models.OneToOneField('Users', on_delete=models.CASCADE) # onetomany relation to the table "Users"
