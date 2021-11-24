from django.urls import path
from . import views

# from rest_framework_jwt.views import obtain_jwt_token

# app_name = 'reviews'

urlpatterns = [
    # path('', views.index, name='index'),
    
    # path('honor/', views.honor, name='honor'),
    path('reviews/', views.review_create_read),
    path('reviews/<int:review_pk>/', views.review_detail_update_delete),
    path('reviews/<int:review_pk>/comment/', views.comment_create_read),
    path('reviews/<int:review_pk>/comment/<int:comment_pk>/', views.comment_detail_update_delete),
    path('reviews/get/<str:user_name>/',views.get)
    # path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    # path('<int:review_pk>/like/', views.like, name='like'),
]