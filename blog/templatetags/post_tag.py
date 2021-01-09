from django import template
from blog.models import post,comment
import os

register = template.Library()
@register.inclusion_tag('blog/lastest_post.html')
def lastest_posts():
    context = {
        'l_posts': post.objects.all()[0:5],

    }
    return context

@register.inclusion_tag('blog/latest_comment.html')
def latest_comments():
    context = {
        'l_comments': comment.objects.filter(active=True)[0:5],
    }
    return context
