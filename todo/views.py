from django.shortcuts import render

# Create your views here.

def todo_list(request):
    return render(request,'todo/todo_list.html')

def todo_detail(request,todo_id):
    return render(request,'todo/todo_detail.html')

def todo_delete_confirm(request,todo_id):
    return render(request,'todo/todo_delete_confirm.html')

def todo_new(request):
    return render(request,'todo/todo_new.html')

def todo_update(request,todo_id):
    return render(request,'todo/todo_update.html')

