from django.test import TestCase
from datetime import datetime
from django.contrib.auth import get_user_model

from ..models import Post, Category
from accounts.models import User, Profile

class TestPostModel(TestCase):
      '''test for post model validation'''

      def test_create_post_with_valid_data(self):
            user = User.objects.create_user(email='test@test.com', password='asd@asd@1234563')
            profile = Profile.objects.create(
                  user = user,
                  first_name = 'test_name',
                  last_name = 'test_last_name',
                  description = 'test_description'
            )

            post = Post.objects.create(
                  author = profile,
                  title = "test", 
                  content = "description", 
                  status = True, 
                  category = None,
                  published_date = datetime.now()
            )

            self.assertEqual(post.title, 'test')
            self.assertEqual(post.content, 'description')
            self.assertEqual(post.author, profile)
            self.assertTrue(post.status)