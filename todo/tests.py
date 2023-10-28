from django.test import TestCase
from todo.models import Task

# Create your tests here.


class TodoListTest(TestCase):
    '''
    todo/todo_list
    へpathが通るか否かcheck
    '''

    def test_should_return_200_httpstatuscode(self):
        response = self.client.get('/todo/todo_list/')
        self.assertEqual(response.status_code, 200)


class Todo_new_test(TestCase):
    '''
    todo/todo_new
    へpathが通るか否かcheck
    '''

    def test_should_return_200_httpstatuscode(self):
        response = self.client.get('/todo/todo_new/')
        self.assertEqual(response.status_code, 200)


class Todo_detail_test(TestCase):
    '''
    todo/todo_detail/<int:todo_id>
    へpathが通るか否かcheck
    '''
    def setUp(self) -> None:
        self.task = Task.objects.create(
            id=2,
            title = "test title",
            description = "this is test description"
        )

    def test_should_return_200_httpstatuscode(self):
        response = self.client.get(f'/todo/todo_detail/{self.task.pk}/')
        self.assertEqual(response.status_code, 200)

class Todo_new_test(TestCase):
    def test_should_return_200_httpstatuscode(self):
        response = self.client.get(f'/todo/todo_new/')
        self.assertEqual(response.status_code, 200)
