from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from app.models import Car

from app.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import *

# Create your views here.
@api_view(['GET','POST'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        'Create': '/product-update/<str:pk>/',
        'Delete': '/product-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def productList(request):
	product = Product.objects.all().order_by('-id')
	serializer = ProductSerilizer(product, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
	product = Product.objects.get(id=pk)
	serializer = ProductSerilizer(product, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
	serializer = ProductSerilizer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
	product = Product.objects.get(id=pk)
	serializer = ProductSerilizer(instance=product, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
	product = Product.objects.get(id=pk)
	product.delete()
	return Response('Item succsesfully delete!')



# @api_view(['GET','POST'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/task-list/',
#         'Detail View': '/task-detail/<str:pk>/',
#         'Create': '/task-update/<str:pk>/',
#         'Delete': '/task-delete/<str:pk>/',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def taskList(request):
# 	tasks = Task.objects.all().order_by('-id')
# 	serializer = TaskSerializer(tasks, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)


# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = TaskSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(instance=task, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)


# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Task.objects.get(id=pk)
# 	task.delete()
# 	return Response('Item succsesfully delete!')


# def index(request):
#     response = json.dumps([{}])
#     return HttpResponse(response, content_type='text/json')



# def get_car(request, car_name):
#     if request.method == 'GET':
#        try:
#            car = Car.objects.get(name=car_name)
#            response = json.dumps([{'Car': car.name, 'Top Speed': car.top_speed}])
#        except:
#             response = json.dumps([{'Error': 'No car with that name'}])
#     return HttpResponse(response, content_type='text/json')

# @csrf_exempt
# def add_car(request):
#     if request.method == "POST":
#         payload = json.loads(request.body)
#         car_name = payload['car_name']
#         top_speed = payload['top_speed']
#         car = Car(name=car_name, top_speed=top_speed)
#         try:
#             car.save()
#             response = json.dumps([{'Success': 'Car added Successfully'}])
#         except:
#             response = json.dumps([{'Error': 'Car could not be added!'}])
#         return HttpResponse(response, content_type='text/json')

