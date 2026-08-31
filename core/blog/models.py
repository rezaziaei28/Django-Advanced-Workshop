from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# Getting user model objects
User = get_user_model()

class Post(models.Model):
    '''
    This is a class to define posts for blog app
    '''
    author = models.ForeignKey("accounts.Profile", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name