from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Users
from datetime import datetime

class UserView(ViewSet):
  def retrieve(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Users.DoesNotExist:
            return Response({'message': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
          
  def list(self, request):
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)       
  
  def create(self, request):
    try:
        # Attempt to parse the created_on date using the correct key
        created_on_date = datetime.strptime(request.data["created_on"], "%Y-%m-%d").date()
    except (KeyError, ValueError):
        # Return an error response if parsing fails
        return Response({"error": "Invalid or missing created_on date. Date format should be YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

    # Attempt to create the user
    user = Users.objects.create(
        first_name=request.data.get("first_name"),
        last_name=request.data.get("last_name"),
        bio=request.data.get("bio"),
        profile_image_url=request.data.get("profile_image_url"),
        email=request.data.get("email"),
        created_on=created_on_date,
        active=request.data.get("active", False),
        is_staff=request.data.get("is_staff", False),
        uid=request.data.get("uid")
    )

    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)   

  def update(self, request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.first_name = request.data["first_name"]
    user.last_name = request.data["last_name"]
    user.bio = request.data["bio"]
    user.profile_image_url = request.data["profile_image_url"]
    user.email = request.data["email"]
    user.active = request.data.get("active", user.active)
    user.is_staff = request.data.get("is_staff", user.is_staff)
    user.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)

    
  def destroy(self, request, pk):
        """Handle DELETE requests for an event"""
        user = Users.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid']
        depth = 2
