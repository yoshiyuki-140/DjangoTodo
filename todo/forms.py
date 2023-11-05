from django import forms
from todo.models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline')
        widgets = {
            'deadline': DateInput()
        }
        error_message = {
            'title': {
                'max_length': f"コメントの文字数が{str(Task.title.field.max_length)}文字を超えているぞ",
                'required': "タイトルを入力してください",
            }
        }
