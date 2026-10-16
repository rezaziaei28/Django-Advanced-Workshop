from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import IndexView, PostDetailView, PostListView
# Create your tests here.

"""class TestUrl(TestCase):
      '''Test urls'''

      def test_blog_index_url_resolve(self):
            '''Test if the blog index URL resolves to IndexView'''
            url = reverse('blog:index')
            self.assertEqual(resolve(url).func.view_class, IndexView) """

class TestUrlWithSimpleTestCase(SimpleTestCase):
      '''Test urls with SimpleTestCase'''

      def test_blog_index_url_resolve(self):
            '''Test if the blog index URL resolves to IndexView'''
            url = reverse('blog:index')
            self.assertEqual(resolve(url).func.view_class, IndexView) 

      def test_blog_post_list_url_resolve(self):
            """Test if the blog post list url resolves to PostListView"""
            url = reverse('blog:post-list')
            self.assertEqual(resolve(url).func.view_class, PostListView) 

      def test_blog_post_detail_url_resolve(self):
            '''Test if the blog index URL resolves to PostDetailView'''
            url = reverse('blog:post-detail', kwargs={'pk': 3})
            self.assertEqual(resolve(url).func.view_class, PostDetailView) 
