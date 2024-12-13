from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.filters import SearchFilter

from .permissions import IsAdminOrReadOnly
from .serializers import *

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def api_root(request, format=None):
   return Response({
       'users': reverse('user-list', request=request, format=format),
       'books': reverse('book-list', request=request, format=format),
       'authors': reverse('author-list', request=request, format=format),
       'genres': reverse('genre-list', request=request, format=format),
       'categories': reverse('category-list', request=request, format=format),
   })

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

class BookViewSet(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
   filter_backends = (SearchFilter,)
   search_fields = ['book_name', 'author__author_name', 'author__author_surname','genre__genre_name']

class AuthorViewSet(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer
   permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

class GenreViewSet(viewsets.ModelViewSet):
   queryset = Genre.objects.all()
   serializer_class = GenreSerializer
   permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   permission_classes = (IsAuthenticated, IsAdminOrReadOnly)