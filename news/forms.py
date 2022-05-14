from tkinter.ttk import Style
from .models import Comment
from django.forms import ModelForm, Textarea, TextInput
from account.models import Liked_post
from django import forms

class ArticleFilterForm(forms.Form):
    find=forms.CharField(label="", required=False)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ( 'body', )

        widgets = {
            "body": Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'style': 'height:15vh; margin-top:1vw;  width: 40vw;'
            })
        }

