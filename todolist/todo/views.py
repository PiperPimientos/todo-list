from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def index(request):
    latest_todo_list = Todo.objects.all()
    return render(request, "todo/index.html", {
        "latest_todo_list": latest_todo_list
    })

def detail(request, todo_id):
    return HttpResponse(f'Estas viendo el To-Do numero {todo_id}')

def results(request, todo_id):
    return HttpResponse(f'El to-do {todo_id} ya fue completado?')