from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tarefas', views.getTask, name='getTask'),
    path('post',views.postTask,name='postTask')
]
