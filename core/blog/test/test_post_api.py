from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse

from accounts.models import User, Profile

class TestPostApi(TestCase):
      '''Test post API endpoints with APIClient'''

      def setUp(self):
            self.user = User.objects.create_user(
                  email='test@test.com', 
                  password='asd@asd@1234563'
            )

      def test_get_post_response_200_status(self):
            '''Test if logged-in user gets 200 status code from post list API'''
            client = APIClient()
            client.force_authenticate(self.user)
            urls = reverse("blog:api_v1:post-list")
            response = client.get(urls)
            self.assertEqual(response.status_code, 200)