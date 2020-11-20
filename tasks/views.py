from django.shortcuts import render
from django.http import HttpResponse
from models import Task, TaskSerializer
from django.shortcuts import render,redirect

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def getTask(request):
    if request.method == 'GET':
        items = Task.objects.all()
        serializer = TaskSerializer(items, many =True)
        return JsonResponse(serializer.data, safe =False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =TaskSerializer(data = data)
  
    if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status =201)
    return JsonResponse(serializer.errors,status = 400)
