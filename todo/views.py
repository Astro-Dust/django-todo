from django.shortcuts import render, redirect
from django.db import connection
from .models import Todo

# READ
def tasks_list(request):
    tasks = Todo.objects.all()
    return render(request, 'tasks.html', {'tasks':tasks})

# CREATE
def create_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Todo.objects.create(name=name)
        return redirect(tasks_list)

# DELETE
def end_task(request, id):

    # TODO: RESETAR id CASO TENHA DELETADO TODOS OS REGISTROS
    # if not Todo.objects.exists():
    #     with connection.cursor() as cursor:
    #         cursor.execute('ALTER TABLE todo_todo AUTO_INCREMENT = 1;')

    task = Todo.objects.get(id=id)
    task.delete()
    return redirect(tasks_list)

# UPDATE

def edit_task(request, id):
    task = Todo.objects.get(id=id)

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        task.name = new_name
        task.save()
        return redirect(tasks_list)
    
    return render(request, 'edit_task.html', {'task' : task})