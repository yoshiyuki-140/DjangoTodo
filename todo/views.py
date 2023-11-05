from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task
from todo.forms import TaskForm

# Create your views here.


def todo_list(request):
    '''
    todo list
    '''
    if request.method == 'POST':
        '''
        追加ボタンが押されたら
        '''
        return redirect('todo_new')

    tasks = Task.objects.all().order_by('deadline')
    return render(request, 'todo/todo_list.html', context={
        'tasks': tasks
    })


def todo_detail(request, todo_id):
    '''
    for showing task's detail
    '''
    # task = Task.objects.get(pk=todo_id)
    task = get_object_or_404(Task, pk=todo_id)

    if request.method == "POST":
        if "delete_task_button" in request.POST:
            '''削除ボタンが押されたら
            '''
            return redirect('todo_delete_confirm', todo_id=todo_id)

        elif "edit_task_button" in request.POST:
            '''編集ボタンが押されたら
            '''
            return redirect('todo_update', todo_id=todo_id)

        elif "redirect_to_HOME" in request.POST:
            '''HOMEへリダイレクトするボタンが押されたら
            '''
            return redirect('todo_list')

        else:
            '''論理的にここに飛んだらエラーだからね
            '''
        
    return render(request, 'todo/todo_detail.html', context={'task': task})


def todo_new(request):
    if request.method == 'POST':
        '''
        タスク追加ボタンが押されたときの処理
        '''
        form = TaskForm(request.POST)
        if form.is_valid():
            '''サニタイズの結果入力が良い状態の時
            '''
            form.save()
            return redirect('todo_list')
        else:
            '''サニタイズの結果入力がよろしくない状態の時
            '''
            messages.add_message(request, messages.WARNING, "そのデータは有効ではないです.")
            return redirect('todo_new')
    else:
        '''
        ボタンが押されていないときの処理
        '''
        form = TaskForm()

    return render(request, 'todo/todo_new.html', context={'form': form})


def todo_delete_confirm(request, todo_id):
    if request.method == "POST":
        if "delete_button" in request.POST:
            task = Task.objects.get(pk=todo_id)
            task.delete()
            return redirect('todo_list')
        else:
            raise Exception("削除ボタンが押されていないのにPOSTされました、おかしい挙動です.")

    return render(request, 'todo/todo_delete_confirm.html')


def todo_update(request, todo_id):
    '''タスクの編集画面
    '''
    task = get_object_or_404(Task, pk=todo_id)
    if request.method == "POST":
        '''
        '''
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_detail', todo_id=todo_id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/todo_update.html', context={'form': form})
