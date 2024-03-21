from django.contrib import admin
from .models import ToDoList, ToDoTasks

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(ToDoTasks)
