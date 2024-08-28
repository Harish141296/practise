from django.urls import path 
from . import views 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/<int:id>', views.detailPost, name='detail'),
]