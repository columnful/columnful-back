import operator

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, get_user_model
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieDetailSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
  movies = Movie.objects.all()
  serializer = MovieListSerializer(movies, many=True)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_id):
  movie = Movie.objects.get(pk=movie_id)
  serializer = MovieDetailSerializer(movie)
  return Response(serializer.data)


@api_view(['POST'])
def like(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  user = request.user

  if movie.like_user.filter(pk=user.pk).exists():
    movie.like_user.remove(user.pk)
    liked = False
  else:
    movie.like_user.add(user.pk)
    liked = True
    
  like_status = {
    'liked': liked,
    'count': movie.like_user.count()
  }
  return JsonResponse(like_status)


@api_view(['GET'])
def recommend_movie_user(request):
  current_user = get_object_or_404(get_user_model(), username=request.user)
  user_preferences = current_user.movies_like.all()
  genres_list = []

  for user_preference in user_preferences:
    genre_preferences = user_preference.movie_id.genres.all()

    for genre_preference in genre_preferences:
      genre = genre_preference.name

      if genre in genres_list:
        genres_list[genre] += 1
      else:
        genres_list[genre] = 1
  
  movies_list = Movie.objects.order_by('-popularity')

  cnt = 0
  movie_recommendation = []
  if genres_list:
    max_genre = max(genres_list.items(), key=operator.itemgetter(1))[0]
    # print(max_genre)
    
    for movie in movies_list:
      target_genre = Genre.objects.get(name=max_genre)
      if target_genre in movie.genres.all():
        if movie not in movie_recommendation:
          movie_recommendation.append(movie)
        cnt += 1
      if cnt == 20: break
  
  serializer = MovieListSerializer(movie_recommendation, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

        
          






@api_view(['GET'])
def recommend_reviews(request):
  pass


@api_view(['GET'])
def recommend_movie_actors(request):
  pass