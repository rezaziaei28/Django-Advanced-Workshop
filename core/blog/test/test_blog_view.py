from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User, Profile
from blog.models import Post, Category

class TestBlogViews(TestCase):
      '''Test views with request'''

      def setUp(self):
            self.user = User.objects.create_user(
                  email='test@test.com', 
                  password='asd@asd@1234563'
            )

            self.profile = Profile.objects.create(
                  user = self.user,
                  first_name = 'test_name',
                  last_name = 'test_last_name',
                  description = 'test_description'
            )

            self.post = Post.objects.create(
                  author = self.profile,
                  title = "test", 
                  content = "description", 
                  status = True, 
                  category = None,
                  published_date=timezone.now()
            )

      def test_blog_index_url_response_successful(self):
            '''check response is successful or not'''
            url = reverse('blog:index')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "index")
            self.assertTemplateUsed(response, template_name = "blog/post_list.html")

      def test_blog_post_detail_is_logged_in_response(self):
            '''logged-in user should be able to see post detail'''

            self.client.force_login(self.user)
            url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200) 

      def test_blog_post_detail_is_anonymouse_response(self):
            '''anonymous user should be redirected to login page'''
            
            url = reverse('blog:post-detail', kwargs={'pk':self.post.id})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
