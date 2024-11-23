from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('authors/', views.author_list),
    path('authors/<int:pk>/', views.author_detail),
    path('genres/', views.genre_list),
    path('genres/<int:pk>/', views.genre_detail),
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail),
]