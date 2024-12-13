from rest_framework import serializers
from .models import Book, Author, Genre, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'password', 'email']
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

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
    books_author = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)
    class Meta:
        model = Author
        fields = ['url', 'id', 'author_name', 'author_surname', 'biography', 'books_author']

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    books_genre = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)
    class Meta:
        model = Genre
        fields = ['url', 'id', 'genre_name', 'books_genre']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    books_category = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)
    class Meta:
        model = Category
        fields = ['url', 'id', 'category_name', 'books_category']