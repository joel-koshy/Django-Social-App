from django.forms import ModelForm
from .models import Post
from django import forms
class PostForm(ModelForm): 
    title = forms.CharField(required=True)
    img=forms.ImageField(required=True)

    class Meta: 
        model=Post 
        fields=['title', 'img']