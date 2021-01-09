from django.contrib import admin
from .models import post,comment
"""
{
     python manage.py createsuperuser
    user: bsh19
    password: 717456393@#$bhs}
"""
# Register your models here.

admin.site.register(post)
admin.site.register(comment)