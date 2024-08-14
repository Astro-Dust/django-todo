from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def tasks_list(request):
    tasks = Todo.objects.all()
    return render(request, 'tasks.html', {'tasks':tasks})

def create_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Todo.objects.create(name=name)
        return redirect(tasks_list)