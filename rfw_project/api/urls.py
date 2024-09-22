from django.urls import path, include 

from .views import get_users, create_user, detail_user

urlpatterns = [
    path('users/', get_users, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', detail_user, name='detail_user'),
]


