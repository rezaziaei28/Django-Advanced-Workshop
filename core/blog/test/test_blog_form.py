from django.test import TestCase
from datetime import datetime

from ..forms import PostForm
from ..models import Category

class TestPostForm(TestCase):
      '''Tests for PostForm validation'''

      def test_post_form_with_valid_data(self):
            '''Form should be valid when all required fields are provided'''
            category_object = Category.objects.create(name='test')
            form = PostForm(data={
                  "title": "test", 
                  "content": "description", 
                  "status": True, 
                  "category": category_object,
                  "published_date": datetime.now()
            })
            # print(form.errors)
            self.assertTrue(form.is_valid())

      def test_post_form_with_no_data(self):
            '''Form should be invalid when no data is provided'''
            form = PostForm(data={})
            # print(form.errors)
            self.assertFalse(form.is_valid())