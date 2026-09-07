from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET','POST'])
def post_list(request):
      '''
      Retrieve and return a single blog post by its ID.
      '''
      if request.method == "GET":
            post = Post.objects.filter(status=True)
            serializer = PostSerializers(post,many=True)
            return Response(serializer.data)
      elif request.method == "POST":
            serializer = PostSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request,id):
      '''
      This function is for show post ID in page 
      '''

      post = get_object_or_404(Post, pk=id, status=True)
      if request.method == "GET":
            serializer = PostSerializers(post)
            return Response(serializer.data)
      elif request.method == "PUT":
            serializer = PostSerializers(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
      elif request.method == "DELETE":
            post.delete()
            return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)

      # try:
      #       post = Post.objects.get(pk=id)
      #       serializer = PostSerializers(post)
      #       return Response(serializer.data)
      # except Post.DoesNotExist:
      #       return Response({"detail":"Post is not exist"}, status=status.HTTP_404_NOT_FOUND)
            
  