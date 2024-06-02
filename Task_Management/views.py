from django.shortcuts import render
from task.models import TaskModel

def ShowTask(request):
    data=TaskModel.objects.all()
    return render(request,"show_task.html",{'data':data})