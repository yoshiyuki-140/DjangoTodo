from django.urls import path
from todo.views import *

urlpatterns = [
    path("todo_list/", todo_list, name="todo_list"),
    path("todo_detail/<int:todo_id>/", todo_detail, name="todo_detail"),
    path("todo_delete_confirm/<int:todo_id>",todo_delete_confirm, name="todo_delete_confirm"),
    path("todo_new/", todo_new, name="todo_new"),
    path("todo_update/<int:todo_id>", todo_update, name="todo_update"),
]
