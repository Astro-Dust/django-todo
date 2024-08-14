from django.shortcuts import render, redirect
from django.db import connection
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
    
def end_task(request, id):

    # TODO: RESETAR id CASO TENHA DELETADO TODOS OS REGISTROS
    # if not Todo.objects.exists():
    #     with connection.cursor() as cursor:
    #         cursor.execute('ALTER TABLE todo_todo AUTO_INCREMENT = 1;')

    task = Todo.objects.get(id=id)
    task.delete()
    return redirect(tasks_list)
