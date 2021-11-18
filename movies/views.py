from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe
from django.core import serializers
from django.http import HttpResponse
from .models import Movie
from django.core.paginator import Paginator
# from django_random_queryset import RandomManager

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # /movies/?page=2 ajax 요청 => json
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = serializers.serialize('json', page_obj)
        return HttpResponse(data, content_type='application/json')
    # /movies/ 첫번째 페이지 요청 => html
    else:
        context = {
            'movies': page_obj,
        }

        return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


# @require_safe
# def recommended(request):
#     queryset = Movie.objects.all()
#     movie = queryset.random(10)
#     context = {
#         'movies' : movie,
#     }
#     return render(request, 'movies/recommended.html', context)
