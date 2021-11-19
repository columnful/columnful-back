from django.urls import path
from . import views

# from rest_framework_jwt.views import obtain_jwt_token

app_name = 'reviews'

urlpatterns = [
    # path('', views.index, name='index'),
    path('honor/', views.honor, name='honor'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:review_pk>/update/', views.update, name='update'),
    path('<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/like/', views.like, name='like'),
]