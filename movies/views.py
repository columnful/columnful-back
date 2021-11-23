from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Movie
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
def review_recommend(request):
  pass

@api_view(['GET'])
def movie_recommend(request):
  pass


@api_view(['GET'])
def recommend_movie_actors(request):
  pass