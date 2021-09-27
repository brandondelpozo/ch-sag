from django.test import TestCase
from django.contrib.auth.models import User
from .models import FieldWorker

class FieldWorkerTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # Create a FieldWorker
        test_field_worker = FieldWorker.objects.create(
            first_name='Worker', last_name='Lastname')
        test_field_worker.save()
    
    def test_field_worker_content(self):
        field_worker = FieldWorker.objects.get(id='f8370eb2-c206-443d-9416-ff6fca97c43a')
        first_name = f'{field_worker.first_name}'
        last_name = f'{field_worker.last_name}'
        self.assertEqual(first_name, 'Worker')
        self.assertEqual(last_name, 'Lastname')