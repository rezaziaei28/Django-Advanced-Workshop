from django.db import models
from accounts.models import User
# Create your models here.

class Post(models.Model):
    '''
    This is a class to define posts for blog app
    '''
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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