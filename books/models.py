from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Author(models.Model):
    """Class representing an author"""

    author = models.CharField(max_length=256)

    def __str__(self):
        return self.author


class Category(models.Model):
    """Class representing a category"""

    category = models.CharField(max_length=256)

    def __str__(self):
        return self.category


class Book(models.Model):
    """Class representing a book"""

    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(Author, blank=True)
    published_date = models.CharField(max_length=10, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    average_rating = models.FloatField(validators=[MaxValueValidator(5.0), MinValueValidator(0.0)], null=True, blank=True)
    ratings_count = models.PositiveIntegerField(blank=True, null=True)
    thumbnail = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
