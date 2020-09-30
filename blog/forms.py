from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        labels = {'author':'名前', 'text':'コメント'}