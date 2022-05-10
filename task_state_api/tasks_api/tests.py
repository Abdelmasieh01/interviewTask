from .models import Task
from rest_framework.test import APITestCase
from rest_framework import status

class TaskTestCase(APITestCase):
    def test_create_task(self):
        data = {'title': 'Testing create.', 'state': Task.active}
        response = self.client.post('/api/tasks/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Testing create.')
        self.assertEqual(Task.objects.get().state, Task.active)

    def test_update_task(self):
        Task.objects.create(title='Testing update.', state=Task.active)
        data = {'title': 'Testing update.', 'state': Task.done}
        response = self.client.put('/api/tasks/1/', data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Task.objects.get().state, Task.done)
    
    def test_update_task_follow_workflow(self):
        Task.objects.create(title='Testing update.', state=Task.archived)
        
        data = {'title': 'Testing update.', 'state': Task.done}
        response = self.client.put('/api/tasks/1/', data)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

        data = {'title': 'Testing update.', 'state': Task.active}
        response = self.client.put('/api/tasks/1/', data)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

        data = {'title': 'Testing update.', 'state': Task.draft}
        response = self.client.put('/api/tasks/1/', data)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)


        Task.objects.create(title='Testing update draft.', state=Task.draft)
        
        data = {'title': 'Testing update draft.', 'state': Task.done}
        response = self.client.put('/api/tasks/2/', data)
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
    
    def test_update_not_found(self):
        Task.objects.create(title='Testing Update, item not found.')
        count = Task.objects.all().count()
        count += 1
        data = {'title': 'Testing update.', 'state': Task.done}
        response = self.client.put('/api/taks/' +  str(count) + '/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_delete_task(self):
        Task.objects.create(title='Testing delete.', state=Task.active)
        response = self.client.delete('/api/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    





        
