from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# pyhon mange.py sqlmigrate blog 0001
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-post_date',)


class comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    text = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"علق {self.name} على {self.post}"
    
    class Meta:
        ordering = ('-comment_date',)
