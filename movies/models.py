from django.db import models
# from django_random_queryset import RandomManager

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    # profile_path = 
    # also_known_as = 

# class Director(models.Model):


class Movie(models.Model):
    # id = models.ImageField(primary_key=True)
    adult = models.BooleanField()
    genres = models.ManyToManyField(Genre)
    original_title = models.CharField(max_length=200)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    actors = models.ManyToManyField(Actor)

    # objects = RandomManager()
