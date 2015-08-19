from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    """Author: Aly Yakan"""
    class Meta:
        model = Comment
        exclude = ('likes_count', 'dislikes_count')
