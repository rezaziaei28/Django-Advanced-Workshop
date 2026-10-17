from django.test import TestCase
from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from ..models import Post, Category
from accounts.models import User, Profile

class TestPostModel(TestCase):
      '''test for post model validation'''

      def setUp(self):
            self.user = User.objects.create_user(email='test@test.com', password='asd@asd@1234563')
            self.profile = Profile.objects.create(
                  user = self.user,
                  first_name = 'test_name',
                  last_name = 'test_last_name',
                  description = 'test_description'
            )
            

      def test_create_post_with_valid_data(self):
            
            post = Post.objects.create(
                  author = self.profile,
                  title = "test", 
                  content = "description", 
                  status = True, 
                  category = None,
                  published_date = datetime.now()
            )
            # Check that post was saved
            self.assertTrue(Post.objects.filter(pk=post.id).exists())
            # Check the field values
            self.assertEqual(post.title, "test")
            self.assertEqual(post.content, "description")
            self.assertEqual(post.author, self.profile)
            self.assertTrue(post.status)


      def test_create_post_with_no_data(self):
            """Test if a post with no data is invalid"""
            post = Post()
            with self.assertRaises(ValidationError):
                  post.full_clean()
