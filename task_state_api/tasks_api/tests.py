from .models import Task
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class TaskTestCase(APITestCase):
    def test_create_task(self):
        data = {'title': 'Testing create.', 'state': 'ac'}
        response = self.client.post('/api/tasks/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Testing create.')
        self.assertEqual(Task.objects.get().state, 'ac')

    def test_update_task(self):
        Task.objects.create(title='Testing update.', state='ac')
        
        data = {'title': 'Testing update.', 'state': 'dn'}
        response = self.client.put('/api/tasks/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Task.objects.get().state, 'dn.')
    
    



        
