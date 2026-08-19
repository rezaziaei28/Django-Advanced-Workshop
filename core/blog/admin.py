from django.contrib import admin
from blog.models import Post,Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'status', 'created_date']
    list_filter = ['author', 'category', 'status']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
