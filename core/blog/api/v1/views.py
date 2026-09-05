from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from ...models import Post
# Create your views here.

data = {
      "id": 1,
      "name": "Zia",
      "job": "backend developer",
}

@api_view()
def post_list(request):
      return Response("ok")

@api_view()
def post_detail(request,id):
      post = Post.objects.get(pk=id)
      serializer = PostSerializers(post)
      return Response(serializer.data)