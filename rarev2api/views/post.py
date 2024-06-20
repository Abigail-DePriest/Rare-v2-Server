from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Post, RareUser
from datetime import datetime


class PostView(ViewSet):
    """Level up post types view"""

    def retrieve(self, request, pk):
       post = Post.objects.get(pk=pk)
       serializer = PostSerializer(post)
       return Response(serializer.data)
     
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post instance
        """

        user = RareUser.objects.get(id=request.data["rare_user"])
        current_date = datetime.now().date()

        post = Post.objects.create(
            rare_user=user,
            title=request.data["title"],
            publication_date=current_date,
            image_url=request.data["image_url"],
            content=request.data["content"],
            # category=request.data["category"],
            approved=request.data["approved"],
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def update(self, request, pk):
        
        
        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.image_url = request.data["image_url"]
        post.content = request.data["content"]
        post.approved = request.data["approved"]
        post.publication_date = request.data["publication_date"]
        rare_user = RareUser.objects.get(pk=request.data["rare_user_id"])
        post.rare_user = rare_user
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
      
class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for post instances"""
    class Meta:
        model = Post
        fields = ('rare_user', 'title', 'publication_date', 'image_url', 'content', 'approved')
