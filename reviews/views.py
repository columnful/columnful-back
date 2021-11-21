from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.http.response import JsonResponse
from .serializers import ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


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


# @api_view(['GET','POST'])
# def comment_create_read(request, review_pk):
#   if request.method == 'POST':
#     review = get_object_or_404(Review, pk=review_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       serializer.save(review=review, user=request.user, username=request.user)
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#   else:
#     review = get_object_or_404(Review, pk=review_pk)
#     comments = review.comment_set.all()
#     serializer = CommentListSerializer(comments, many=True)


# @api_view(['GET', 'PUT', 'DELETE'])
# def comment_detail_update_delete(request, review_pk, comment_pk):
#   comment = get_object_or_404(Comment, pk=comment_pk)
#   if request.method == 'GET':
#     serializer = CommentSerializer(comment)
#     return Response(serializer.data)
#   else:
#     if request.user == comment.user:
#       if request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#           serializer.save()
#           return Response(serializer.data)
#       else:
#         comment.delete()
#         return Response({'message': f'{comment_pk}번 댓글이 정상적으로 삭제되었습니다.', 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)
#     else:
#         return Response({'error':'니가 쓴 댓글 아니잖아.'}, status=status.HTTP_401_UNAUTHORIZED)


# 여기부터 쓸모없음

# @require_GET
# def detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     comments = review.comment_set.all()
#     comment_form = CommentForm()
#     context = {
#         'review': review,
#         'comment_form': comment_form,
#         'comments': comments,
#     }
#     return render(request, 'reviews/detail.html', context)


# @require_http_methods(['POST', 'GET'])
# def update(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     if request.method == "POST":
#         form = ReviewForm(request.POST, instance = review)
#         if form.is_valid():
#             review = form.save()
#             return redirect('reviews:detail', review.pk)
#     else:
#         form = ReviewForm(instance = review)
#     context = {
#         'form': form,
#         'review': review,
#     }
#     return render(request, 'reviews/update.html', context)

# @require_POST
# def delete(request, review_pk):
#     movie = get_object_or_404(Review, pk=review_pk)
#     movie.delete()
#     return redirect('reviews:index')


# @require_POST
# def create_comment(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.review = review
#         comment.user = request.user
#         comment.save()
#         return redirect('reviews:detail', review.pk)
#     context = {
#         'comment_form': comment_form,
#         'review': review,
#         'comments': review.comment_set.all(),
#     }
#     return render(request, 'reviews/detail.html', context)


# @require_POST
# def like(request, review_pk):
#     if request.user.is_authenticated:
#         review = get_object_or_404(Review, pk=review_pk)
#         user = request.user

#         if review.like_users.filter(pk=user.pk).exists(): 
#             review.like_users.remove(user)
#             is_like = False
#         else:
#             review.like_users.add(user)
#             is_like = True

#         like_counter = review.like_users.count()
#         return JsonResponse({
#             'success' : True,
#             'isLike' : is_like,
#             'likeCounter' : like_counter,
#         })
#     return redirect('accounts:login')


# def honor(request):
#     reviews = Review.objects.order_by('-pk')
#     context = {
#         'reviews': reviews,
#     }
#     return render(request, 'reviews/index.html', context)
