from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view()
def post_list(request):
      return Response("ok")


@api_view()
def post_detail(request,id):
      post = get_object_or_404(Post, pk=id)
      post = Post.objects.get(pk=id)
      serializer = PostSerializers(post)
      return Response(serializer.data)

      # try:
      #       post = Post.objects.get(pk=id)
      #       serializer = PostSerializers(post)
      #       return Response(serializer.data)
      # except Post.DoesNotExist:
      #       return Response({"detail":"Post is not exist"}, status=status.HTTP_404_NOT_FOUND)
            
  