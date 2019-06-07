from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog.as_view(), name='blog'),
    path('quote_added', views.quote_added, name='quote_added'),
]