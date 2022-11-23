from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(AbstractUser):
    pass

class List(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mylists')
    # contributors = models.

class ListItem(models.Model):
    # Define media type options
    media_types = [
    ('M', 'Movie'),
    ('S', 'Show'),
    ]

    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item = models.IntegerField() # will be the ID, so you can look for a Media object or search TMDB
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=media_types)

class Media(models.Model):
    # Define media type options
    media_types = [
    ('M', 'Movie'),
    ('S', 'Show'),
    ]

    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20, choices=media_types) #needs options: movie, tv
    poster = models.URLField()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10)])