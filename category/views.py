from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def AddCategory(request):
    if request.method=="POST":
        category_form=forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect("AddCategory")
        
    else:
        category_form=forms.CategoryForm()        
    return render(request,"category/add_category.html",{'form':category_form})
