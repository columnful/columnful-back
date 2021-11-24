import json

from django.db import models
from django.conf import settings



class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.TextField(null=True)
    # also_known_as = 


class Director(models.Model):
    name= models.CharField(max_length=100)
    profile_path = models.TextField(null=True)


class Movie(models.Model):
    # id = models.IntegerField(primary_key=True)
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200)
    genres_ids = models.ManyToManyField(Genre)
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=200)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movie", default=None)

    # actors = models.ManyToManyField(Actor)

    # directors = models.ManyToManyField(Director)
    # keywords = models.TextField(blanck=True, null=True, default='{}')

    def __str__(self):
        return self.title
