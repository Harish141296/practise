from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse(f"You are looking at the Question : {question_id}")

def results(request, question_id):
    response = "You are looking at the Result Question: %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")