from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializers
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

# Create your views here.

"""@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
      '''
      Getting a list of posts and creating a new post
      '''

      if request.method == "GET":
            '''Retrveing a list of post'''

            post = Post.objects.filter(status=True)
            serializer = PostSerializers(post,many=True)
            return Response(serializer.data)
      elif request.method == "POST":
            serializer = PostSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
"""

""" Function base views for update and delede post
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
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
"""    

class PostList(APIView):
      '''
      Getting a list of posts and creating a new post
      '''

      permission_classes = [IsAuthenticatedOrReadOnly]  # This code about login user in site
      serializer_class = PostSerializers # This code is for esay access for change postt

      def get(self, request):
            '''Retrveing a list of post'''
            post = Post.objects.filter(status=True)
            serializer = PostSerializers(post, many=True)
            return Response(serializer.data)

      def post(self, request):
            '''Creating a post with provided data'''
            serializer = PostSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
      

class PostDetail(APIView):
      '''
      This class for getting detail of the post and edite and removing it
      '''

      permission_classes = [IsAuthenticatedOrReadOnly]  # This code is about login user in site
      serializer_class = PostSerializers # This code is for esay access for change postt


      def get(self, request,id):
            '''Retrveing the post data'''
            post = get_object_or_404(Post, pk=id,status=True)
            serializer = self.serializer_class(post)
            return Response(serializer.data)

      def put(self,request,id):
            '''editing the post data'''
            post = get_object_or_404(Post, pk=id,status=True)
            serializer = self.serializer_class(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

      def delete(self, request,id):
            '''Deleting the post object'''
            post = get_object_or_404(Post, pk=id, status=True)
            post.delete()
            return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)
      
