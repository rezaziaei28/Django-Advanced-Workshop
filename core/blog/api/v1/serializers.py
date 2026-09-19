from rest_framework import serializers
from blog.models import Post,Category

# class PostSerializers(serializers.Serializer):
#       id = serializers.IntegerField()
#       title = serializers.CharField(max_length=255)
class CategorySerializers(serializers.ModelSerializer):

      class Meta:
            model = Category
            fields = ['id', 'name']

class PostSerializers(serializers.ModelSerializer):

      snippet = serializers.ReadOnlyField(source='get_snippet')
      relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
      absolute_url = serializers.SerializerMethodField()

      # category = CategorySerializers()
      # category = serializers.SlugRelatedField(many=False,slug_field='name', queryset=Category.objects.all())

      # this for adding read only fields
      # author = serializers.ReadOnlyField() this is equal bottom author
      # author = serializers.CharField(read_only=True)

      class Meta:
            model = Post
            fields = ['id', 'author', 'relative_url', 'absolute_url',
                      'snippet', 'title', 'category','content', 'status', 'created_date', 'published_date']
            read_only_fields = ['author',]

      def get_absolute_url(self, object):
            request = self.context.get('request')
            return request.build_absolute_uri(object.pk)

      def to_representation(self, instance):
            rep = super().to_representation(instance)
            rep['category'] = CategorySerializers(instance.category).data
            rep.pop('snippet', None)
            return rep
