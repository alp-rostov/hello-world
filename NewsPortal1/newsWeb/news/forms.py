from django import forms
from .models import Author
from .models import Post, Category

class Create_news(forms.ModelForm):
    id_author = forms.ModelChoiceField(
        label='Автор',
        queryset=Author.objects.order_by ( '-full_name' ).all ( ),
        empty_label='Выберите автора',
    )
    head_article=forms.CharField(
        label='Название - заголовок'
    )
    text_post=forms.CharField(label='Текст', widget=forms.Textarea)

    category= forms.ModelMultipleChoiceField(
        label='Категория',
        queryset=Category.objects.order_by ( 'name' ).all ( ),
        widget=forms.CheckboxSelectMultiple

    )

    class Meta:
        model = Post
        fields = [
            'head_article',
            'text_post',
            'id_author',
            'category'
        ]

    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     text_post = cleaned_data.get("text_post")
    #     if text_post is not None and len(text_post) < 20:
    #         raise ValidationError({
    #             "description": "Текст не может быть менее 20 символов."
    #         })
    #     return cleaned_data