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
            created_on_date = datetime.strptime(request.data["createdOn"], "%Y-%m-%d").date()
        except (KeyError, ValueError):
            return Response({"error": "Invalid or missing createdOn date. Date format should be YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Required fields
        required_fields = ["first_name", "last_name", "email", "uid"]
        for field in required_fields:
            if field not in request.data:
                return Response({"error": f"Missing required field: {field}"}, status=status.HTTP_400_BAD_REQUEST)

        # Optional fields with defaults
        bio = request.data.get("bio", "")
        profile_image_url = request.data.get("profile_image_url", "")
        active = request.data.get("active", False)
        is_staff = request.data.get("is_staff", False)

        # Create a new user
        user = Users.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            bio=bio,
            profile_image_url=profile_image_url,
            email=request.data["email"],
            created_on=created_on_date,
            active=active,
            is_staff=is_staff,
            uid=request.data["uid"]
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
