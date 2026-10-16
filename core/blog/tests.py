from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import IndexView
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
