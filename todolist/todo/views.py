from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def index(request):
    latest_todo_list = Todo.objects.all()
    if request.method == "POST":    
        if "taskAdd" in request.POST:
            content = request.POST["description"]
            content = Todo
            content.save()
            # Me pide un positional argument self para poder agregar el nuevo task
            return redirect("/")
    return render(request, "todo/index.html", {
        "latest_todo_list": latest_todo_list,
    })

def detail(request, todo_id):
    return HttpResponse(f'Estas viendo el To-Do numero {todo_id}')

def results(request, todo_id):
    return HttpResponse(f'El to-do {todo_id} ya fue completado?')