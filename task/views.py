from django.shortcuts import render,redirect
from .import forms
from . import models


# Create your views here.
def AddTask(request):
    if request.method=="POST":
        task_form= forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("AddTask") 
    else:
        task_form= forms.TaskForm() 
    return render(request,"task/add_task.html",{'form': task_form})


def EditTask(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task_form=forms.TaskForm(instance=task)
    if request.method=="POST":
        task_form= forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("homepage")
        
    return render(request,"task/add_task.html",{'form': task_form})


def DeleteTask(request, id):
    task = models.TaskModel.objects.get(pk=id) 
    task.delete()
    return redirect('homepage')
