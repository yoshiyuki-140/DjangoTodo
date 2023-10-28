from django.shortcuts import render, redirect
from todo.models import Task

# Create your views here.


def todo_list(request):
    if request.method == 'POST':
        redirect('todo_new')
    tasks = Task.objects.all()
    return render(request, 'todo/todo_list.html', context={
        'tasks': tasks
    })


def todo_detail(request, todo_id):
    task = Task.objects.get(pk=todo_id)

    # タスクの削除ボタンが押されたときの処理
    if request.method == "POST":
        task.delete()
        # todo_listへリダイレクト
        return redirect('todo_list')

    return render(request, 'todo/todo_detail.html', context={'task': task})


def todo_new(request):
    if request.method == 'POST':
        '''
        ここはバリデーションやサニタイズの処理が必要
        '''

        model_instance = Task.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )
        model_instance.save()
        return redirect('todo_list')

    return render(request, 'todo/todo_new.html')


def todo_delete_confirm(request, todo_id):
    if request.method == "POST":
        task = Task.objects.get(pk=todo_id)
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_delete_confirm.html')

def todo_update(request, todo_id):
    return render(request, 'todo/todo_update.html')
