from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Posts, Users
from datetime import datetime


class PostsView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
       post = Posts.objects.get(pk=pk)
       serializer = PostsSerializer(post)
       return Response(serializer.data)
     
    def list(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """

        user = Users.objects.get(id=request.data["rare_user"])
        current_date = datetime.now().date()

        post = Posts.objects.create(
            rare_user=user,
            title=request.data["title"],
            publication_date=current_date,
            image_url=request.data["image_url"],
            content=request.data["content"],
            # category=request.data["category"],
            approved=request.data["approved"],
        )
        serializer = PostsSerializer(post)
        return Response(serializer.data)
      
      
class PostsSerializer(serializers.ModelSerializer):
    """JSON serializer for game instances"""
    class Meta:
        model = Posts
        fields = ('rare_user', 'title', 'publication_date', 'image_url', 'content', 'approved')
