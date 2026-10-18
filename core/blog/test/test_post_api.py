from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User, Profile

class TestPostApi(TestCase):
      '''Test post API endpoints with APIClient'''

      def setUp(self):
            self.client = APIClient()
            self.user = User.objects.create_user(
                  email='test@test.com', 
                  password='asd@asd@1234563'
            )

            # self.profile = Profile.objects.create(
            #       user = self.user,
            #       first_name = 'test_name',
            #       last_name = 'test_last_name',
            #       description = 'test_description'
            # )
            self.profile = Profile.objects.get(user=self.user)


      def test_get_post_response_200_status(self):
            '''Test if logged-in user gets 200 status code from post list API'''
            self.client.force_authenticate(self.user)
            urls = reverse("blog:api_v1:post-list")
            response = self.client.get(urls)
            self.assertEqual(response.status_code, 200)

      
      def test_create_post_response_201_status(self):
            '''Test if logged-in user can create a post'''
            self.client.force_authenticate(self.user)
            urls = reverse("blog:api_v1:post-list")
            data={
                  "author": self.user,
                  "title": "test create api",
                  "content": "test content create api",
                  "status": True,
                  "published_date": timezone.now()
            }
            response = self.client.post(urls, data)
            self.assertEqual(response.status_code, 201)

      def test_create_post_response_403_status(self):
            '''Test if anonymous user gets 403 when creating a post'''
            urls = reverse("blog:api_v1:post-list")
            data = {"title": "test"}
            response = self.client.post(urls, data)
            self.assertEqual(response.status_code, 403)