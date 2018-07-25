from django.urls import path
from . import views

urlpatterns = [

    # localhost:8000/article/1
    path('<int:article_id>', views.simple_article_detail, name="simple_article_detail"),

    # localhost:8000/article/
    path('', views.article_list, name="article_list"),

    path('type/<int:blog_type_pk>',  views.blog_with_type, name="blog_with_type"),
]