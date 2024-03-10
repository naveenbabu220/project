from django.test import TestCase
from rest_framework.test import APIClient
from .models import Document
from rest_framework import status
# Create your tests here.

class DocumentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.document1 = Document.objects.create(title='Test Document 1', content='Content 1', status='draft')
        self.document2 = Document.objects.create(title='Test Document 2', content='Content 2', status='published')

    def test_get_all_documents(self):
        response = self.client.get('/api/documents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming 2 documents are created in setUp

    def test_get_single_document(self):
        response = self.client.get(f'/api/documents/{self.document1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Document 1')

    def test_create_document(self):
        data = {'title': 'New Document', 'content': 'New Content', 'status': 'draft'}
        response = self.client.post('/api/documents/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 3)  # Assuming 2 documents are created in setUp

    def test_update_document(self):
        data = {'title': 'Updated Document', 'content': 'Updated Content', 'status': 'published'}
        response = self.client.put(f'/api/documents/{self.document1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Document')
        self.assertEqual(response.data['status'], 'published')

    def test_delete_document(self):
        response = self.client.delete(f'/api/documents/{self.document1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Document.objects.count(), 1)  # One document should be deleted

