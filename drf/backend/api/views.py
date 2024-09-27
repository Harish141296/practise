from django.shortcuts import render
from django.http import JsonResponse
import json 
from products.models import Product
from django.forms.models import model_to_dict

# Create your views here.
def api_home_demo(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        print("not convertable data")
    print(body)
    print(request.GET)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    # return JsonResponse({"message":"Hi there Master, Welcome back world needs your skill."})
    return JsonResponse(data)

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title 
        # data['content'] = model_data.content
        # data['price'] = model_data.price 
        data_all = model_to_dict(model_data)
        print(data_all)
        #if we want particular field, we can pass those column as an argument 
        data = model_to_dict(model_data, fields=['id','title','price'])

    return JsonResponse(data)