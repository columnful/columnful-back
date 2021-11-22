from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # path('', views.movie_home),
    path('', views.movie_list),

    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/like/', views.like),
    
    path('movie_recommend/', views.movie_recommend),
    path('review_recommend/', views.review_recommend),
]