from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel
from .forms import StudentForm
from django.shortcuts import render,redirect

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


def CreateView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data')
    else:
        form =StudentForm()
        context = {
            'form':form
        }
        return render(request,'create.html',context)
