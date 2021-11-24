from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.http.response import JsonResponse
from .serializers import ReviewSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# @require_GET
# def index(request):
#     reviews = Review.objects.order_by('-pk')
#     context = {
#         'reviews': reviews,
#     }
#     return render(request, 'reviews/index.html', context)


@api_view(['GET', 'POST'])
def review_create_read(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, username=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        reviews = Review.objects.order_by('-pk')
        serializer= ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if request.method == 'GET':
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
  else:
    if request.user == review.user:
      if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
        review.delete()
        return Response({'message': f'{review_pk}번 댓글이 정상적으로 삭제되었습니다.', 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response({'error':'니가 쓴 글 아니잖아.'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def comment_create_read(request, review_pk):
  if request.method == 'POST':
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(review=review, user=request.user, username=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  else:
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, review_pk, comment_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)
  if request.method == 'GET':
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
  else:
    if request.user == comment.user:
      if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data)
      else:
        comment.delete()
        return Response({'message': f'{comment_pk}번 댓글이 정상적으로 삭제되었습니다.', 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response({'error':'니가 쓴 댓글 아니잖아.'}, status=status.HTTP_401_UNAUTHORIZED)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get(request, user_name):
  User = get_user_model()
  person = get_object_or_404(User, username=user_name)
  reviews = Review.objects.filter(username_id=person.username).order_by('-pk')
  serializer= ReviewSerializer(reviews, many=True)
  return Response(serializer.data)