from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .models import Category
from .views import *

user_list = UserViewSet.as_view({
   'get': 'list',
   'post': 'create'
})
user_detail = UserViewSet.as_view({
   'get': 'retrieve',
    'delete': 'destroy'
})

book_list = BookViewSet.as_view({
   'get': 'list',
   'post': 'create'
})
book_detail = BookViewSet.as_view({
   'get': 'retrieve',
   'put': 'update',
   'patch': 'partial_update',
   'delete': 'destroy'
})

author_list = AuthorViewSet.as_view({
   'get': 'list',
   'post': 'create'
})
author_detail = AuthorViewSet.as_view({
   'get': 'retrieve',
   'put': 'update',
   'patch': 'partial_update',
   'delete': 'destroy'
})

genre_list = GenreViewSet.as_view({
   'get': 'list',
   'post': 'create'
})
genre_detail = GenreViewSet.as_view({
   'get': 'retrieve',
   'put': 'update',
   'patch': 'partial_update',
   'delete': 'destroy'
})

category_list = CategoryViewSet.as_view({
   'get': 'list',
   'post': 'create'
})
category_detail = CategoryViewSet.as_view({
   'get': 'retrieve',
   'put': 'update',
   'patch': 'partial_update',
   'delete': 'destroy'
})

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('authors/', author_list, name='author_list'),
    path('authors/<int:pk>/', author_detail, name='author_detail'),
    path('genres/', genre_list, name='genre_list'),
    path('genres/<int:pk>/', genre_detail, name='genre_detail'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)