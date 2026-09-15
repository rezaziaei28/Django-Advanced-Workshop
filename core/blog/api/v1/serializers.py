from rest_framework import serializers
from blog.models import Post,Category

# class PostSerializers(serializers.Serializer):
#       id = serializers.IntegerField()
#       title = serializers.CharField(max_length=255)

class PostSerializers(serializers.ModelSerializer):

      snippet = serializers.ReadOnlyField(source='get_snippet')
      relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)

      # this for adding read only fields
      # author = serializers.ReadOnlyField() this is equal bottom author
      # author = serializers.CharField(read_only=True)

      class Meta:
            model = Post
            fields = ['id', 'author', 'relative_url','snippet', 'title', 'content', 'status', 'created_date', 'published_date']
            read_only_fields = ['author',]
class CategorySerializers(serializers.ModelSerializer):

      class Meta:
            model = Category
            fields = ['id', 'name']