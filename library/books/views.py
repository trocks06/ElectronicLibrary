from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import *
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

class BookViewSet(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):
   queryset = Genre.objects.all()
   serializer_class = GenreSerializer

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer