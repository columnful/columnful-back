from .models import Movie, Actor, Director, Genre
from rest_framework import serializers

# class MovieTitleSerializer(serializers.ModelSerializer):

#   class Meta:
#     model = Movie
#     fields = ('title','id',)

class MovieListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = ('title', 'poster_path', 'id', 'vote_average')


class MovieDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = '__all__'