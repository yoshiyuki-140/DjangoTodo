from django.shortcuts import render
from todo.models import Task

# Create your views here.


def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/todo_list.html', context={
        'tasks': tasks
    })


def todo_detail(request, todo_id):
    task = Task.objects.get(pk=todo_id)
    return render(request, 'todo/todo_detail.html', context={
        'task': task
    })


def todo_delete_confirm(request, todo_id):
    return render(request, 'todo/todo_delete_confirm.html')


def todo_new(request):
    return render(request, 'todo/todo_new.html')


def todo_update(request, todo_id):
    return render(request, 'todo/todo_update.html')
