from rest_framework import serializers
from .models import Genre, Movie, Actor, Director


class MovieListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = ('title', 'poster_path', 'id', 'vote_average')


class MovieDetailSerializer(serializers.ModelSerializer):

  class GenreSerializer(serializers.ModelSerializer):
    class Meta:
      model = Genre
      fields = '__all__'

  class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
      model = Director
      fields = '__all__'

  class ActorSerializer(serializers.ModelSerializer):
    class Meta:
      model = Actor
      fields = '__all__'

  genre_ids = GenreSerializer(many=True, read_only=True)
  directors = DirectorSerializer(many=True, read_only=True)
  actors = ActorSerializer(many=True, read_only=True)

  class Meta:
    model = Movie
    fields = '__all__'