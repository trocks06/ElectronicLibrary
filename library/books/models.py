from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    release_year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_covers')
    file = models.FileField(upload_to='book_files')

    class Meta:
        unique_together = ('book_name', 'author', 'release_year', 'publisher')

class Author(models.Model):
    author_name = models.CharField(max_length=100, unique=True)
    author_surname = models.CharField(max_length=100, unique=True)
    biography = models.TextField(default='Информация отсутствует')

class Genre(models.Model):
    genre_name = models.CharField(max_length=100, null=True, blank=True, unique=True)

class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True, unique=True)