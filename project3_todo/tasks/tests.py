from django.test import TestCase
from .models import Task 
from django.urls import reverse 


# Create your tests here.

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title = "Test task",
            description = "This is the test task.",
            completed = False 
        )
    
    def test_task_completed(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is the test task.")
        self.assertFalse(task.completed)
        self.assertIsNotNone(task.create_at)
        self.assertIsNotNone(task.updated_at)


class TaskViewTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title = "Test task.",
            description = "This is the test task.",
            completed = False 
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.title)

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)

    def test_task_create_view(self):
        response = self.client.get(reverse('task_create'), {
            'title': 'New Task',
            'description':'This is a new Task',
            'completed' : False 
        })
        self.assertEqual(response.status_code, 200) # Redirects after successful creation
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_update_view(self):
        response = self.client.get(reverse('task_update', args=[self.task.id]),{
            'title' : 'Updated Task',
            'description' : 'This is an updated Task',
            'completed' : True
        })
        self.assertEqual(response.status_code, 200) # Redirects after successful creation
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.description, 'This is an updated Task')
        self.assertTrue(self.task.completed)

    def test_task_delete_view(self):
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    

