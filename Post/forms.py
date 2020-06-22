from . import models
from django import forms
from django.forms import ModelForm
from .models import Post
class Post_form(ModelForm):
    class Meta:
        model=Post
        fields=('__all__')
