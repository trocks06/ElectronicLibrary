from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.ForeignKey('Author', related_name="books_author", on_delete=models.CASCADE)
    release_year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    genre = models.ForeignKey('Genre', related_name="books_genre", on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name="books_category", on_delete=models.CASCADE)
    publisher = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_covers')
    file = models.FileField(upload_to='book_files')

    class Meta:
        unique_together = ('book_name', 'author', 'release_year', 'publisher')

    def __str__(self):
        return self.book_name

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_surname = models.CharField(max_length=100)
    biography = models.TextField(default='Информация отсутствует')

    class Meta:
        unique_together = ('author_name', 'author_surname')

    def __str__(self):
        return self.author_name + ' ' + self.author_surname

class Genre(models.Model):
    genre_name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    def __str__(self):
        return self.genre_name

class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    def __str__(self):
        return self.category_name