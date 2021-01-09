from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,  name='home'),
    path('about/',views.about, name = 'about'),
    path('details/<int:post_id>/', views.post_detail, name = 'details'),
]