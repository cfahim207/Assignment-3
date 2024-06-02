from django.urls import path,include
from .import views
urlpatterns = [
    
    path('add/', views.AddTask, name="AddTask"),
    path('edit/<int:id>', views.EditTask, name="EditTask"),
    path('delete/<int:id>', views.DeleteTask, name="DeleteTask"),
    
]