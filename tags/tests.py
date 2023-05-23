from django.test import TestCase

# Create your tests here.

from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

class MyAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        

    def test_GetTagList(self):
        url = reverse('/api/v1/tags/get')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK) 
    
    def test_CreateTag(self):
        url = reverse("/api/v1/tags/create")
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_DeleteTag(self):
        url = reverse("/api/v1/tags/delete")
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK) 