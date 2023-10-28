from django.test import TestCase

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
