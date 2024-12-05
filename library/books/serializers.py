from rest_framework import serializers
from .models import Book, Author, Genre, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author_name', 'author_surname', 'biography']

class GenreSerializer(serializers.ModelSerializer):
    genre_name = serializers.HyperlinkedIdentityField(view_name='genre_detail')
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book_detail', read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'genre_name', 'books']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class BookSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author', 'release_year', 'genre', 'category', 'publisher', 'image', 'file']


    def validate(self, attrs):
        if attrs['category'] == 'Textbook':
            if Book.objects.filter(
                title=attrs['title'],
                publisher=attrs['publisher'],
                publication_year=attrs['publication_year']
            ).exists():
                raise serializers.ValidationError("Учебник с таким изданием уже существует!")
        return attrs
