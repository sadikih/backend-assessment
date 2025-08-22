from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item

class ItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item = Item.objects.create(name="Test Item")
        self.list_url = reverse('item-list')  # comes from router
        self.detail_url = reverse('item-detail', args=[self.item.id])

    def test_list_items(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_create_item(self):
        response = self.client.post(self.list_url, {"name": "New Item"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)

    def test_update_item(self):
        response = self.client.put(self.detail_url, {"name": "Updated Item"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Updated Item")

    def test_delete_item(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)
