from django.contrib import admin
from .models import Post, Category, Comments, PostCategory, Author


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('pk', 'head_article','text_post','date', 'type_post', 'sum_rank', 'id_author') # генерируем список имён всех полей для более красивого отображения

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text','date','sum_rank','id_users']
    list_filter = ['id_users']
    # search_fields = ['id_users']

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'id_post','id_category') # генерируем список имён всех полей для более красивого отображения
    list_filter = ['id_category']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Author)
