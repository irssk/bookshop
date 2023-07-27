from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}, {self.surname}'

class Genre(models.Model):
    genre = models.CharField(max_length=20)
    average_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f'{self.genre}, {self.average_rating}'

class Book(models.Model):
    name = models.CharField(max_length=50, default="Unknown book", null=False)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    price = models.IntegerField(default=0)
    author = models.OneToOneField(Author, on_delete=models.PROTECT)
    genre = models.OneToOneField(Genre, on_delete=models.PROTECT)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.author}'

    def save(self):
        self.slug = slugify(self.name)
        super().save()



