from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_view(request):
    details = {'name': 'Jerry',
               'profession': 'Senior'}
    return render(request, 'views/main.html', context = details)