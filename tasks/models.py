from rest_framework import serializers
from .models import ItemModel
 
# Create your models here.


class Task(serializers.Model):
    title = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField('date published')
    description = serializers.CharField(max_length=500)

class TaskForm(serializers.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'pub_date','description']