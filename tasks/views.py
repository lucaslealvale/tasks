from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task, TaskSerializer
from django.shortcuts import render,redirect
from rest_framework.parsers import JSONParser
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def getTask(request):
    
    items = Task.objects.all()
    serializer = TaskSerializer(items, many =True)
    return JsonResponse(serializer.data, safe =False)

@csrf_exempt
def postTask(request):

    data = JSONParser().parse(request)
    serializer =TaskSerializer(data = data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status =201)
    return JsonResponse(serializer.errors,status = 401)