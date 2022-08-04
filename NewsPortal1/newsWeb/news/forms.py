from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class Create_news(forms.ModelForm):
    # type_post= forms.CharField ( widget=forms.HiddenInput ( ), required=False, initial='')

    class Meta:
        model = Post
        fields = [
            'head_article',
            'text_post',
            'id_author',
            # 'type_post'
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