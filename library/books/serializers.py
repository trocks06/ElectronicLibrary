from unicodedata import category

from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField

from .models import Book, Author, Genre, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['url', 'id', 'book_name', 'author', 'release_year', 'genre', 'category', 'publisher', 'image', 'file']

    def validate(self, attrs):
        category = attrs['category']
        if category.category_name == 'Учебник':
            if Book.objects.filter(
                book_name=attrs['book_name'],
                publisher=attrs['publisher'],
                release_year=attrs['release_year']
            ).exists():
                raise serializers.ValidationError("Учебник с таким изданием уже существует!")
        return attrs

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = HyperlinkedRelatedField(view_name='books_detail', many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['url', 'id', 'author_name', 'author_surname', 'biography', 'books']

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)
    class Meta:
        model = Genre
        fields = ['url', 'id', 'genre_name', 'books']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)
    class Meta:
        model = Category
        fields = ['url', 'id', 'category_name', 'books']