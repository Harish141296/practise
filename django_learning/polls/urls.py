from django.urls import path
from .views import index, detail, vote, results

urlpatterns = [
    path('index/', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name = 'results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]



