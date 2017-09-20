from django.db import models
from django.utils import timezone
from django import forms


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    picture = models.FileField( null=True, blank = True)
    words_to_cut=10

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    def get_cut(self):
        return ((' '.join(self.text.split(' ')[:self.words_to_cut]))+'...'*(self.words_to_cut < len(self.text.split(' '))))

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
