from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('api-token-auth/', obtain_jwt_token),
    path('profile/<str:user_name>/', views.profile),
    path('profile/<str:user_name>/follow/', views.follow),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('<username>/', views.profile, name='profile'),
    # path('<int:user_pk>/follow/', views.follow, name='follow'),
]
