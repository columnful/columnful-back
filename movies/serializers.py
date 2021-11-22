from .models import Genre, Movie, Actor, Director
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