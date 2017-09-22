from django import forms
from .models import Post, Comment, TestFileContainer

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','picture',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ContForm(forms.ModelForm):

    class Meta:
        model = TestFileContainer
        fields = ('cont',)
