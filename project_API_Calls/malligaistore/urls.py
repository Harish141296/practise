from django.urls import path 
from .views import myapiCall

urlpatterns = [
    path('', myapiCall, name='myapiCall'),
]