from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Animal

class ShelterTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(
            username="testuser", password="pass"
        )
        testuser.save()

        test_animal = Animal.objects.create(
            name="Tokyo",
            owner=testuser,
            description="Pretty skittish, occasionally will bite and scratch"
        )
        test_animal.save()
    
    def setUp(self):
        self.client.login(username="testuser", password="pass")


    def test_animal_model(self):
        animal=Animal.objects.get(id=1)
        actual_owner = str(animal.owner)
        actual_name = str(animal.name)
        actual_description = str(animal.description)
        self.assertEqual(actual_owner, 'testuser')
        self.assertEqual(actual_name, 'Tokyo')
        self.assertEqual(actual_description, 'Pretty skittish, occasionally will bite and scratch')


    def test_get_animal_list(self):
        url = reverse('animal_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        animals = response.data
        self.assertEqual(len(animals), 1)
        self.assertEqual(animals[0]["name"], 'Tokyo')


    def test_get_animal_by_id(self):
        url = reverse('animal_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        animal = response.data
        self.assertEqual(animal["name"], 'Tokyo')


    def test_authentication_required(self):
        self.client.logout()
        url = reverse('animal_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)