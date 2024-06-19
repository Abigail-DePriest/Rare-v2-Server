from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import RareUser

class RareUserView(ViewSet):
  def retrieve(self, request, pk):
        try:
            user = RareUser.objects.get(pk=pk)
            serializer = RareUserSerializer(user)
            return Response(serializer.data)
        except RareUser.DoesNotExist:
            return Response({'message': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
          
  def list(self, request):
        users = RareUser.objects.all()
               
        serializer = RareUserSerializer(users, many=True)
        return Response(serializer.data)       
  
  def create(self, request):
   
    user = RareUser.objects.create(
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        bio=request.data["bio"],
        profile_image_url=request.data["profile_image_url"],
        email=request.data["email"],
        active=request.data.get("active", True),
        is_staff=request.data.get("is_staff", False),
        uid=request.data["uid"]
    )
    serializer = RareUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)   

  def update(self, request, pk):
    try:
        user = RareUser.objects.get(pk=pk)
    except RareUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.first_name = request.data.get("first_name", user.first_name)
    user.last_name = request.data.get("last_name", user.last_name)
    user.bio = request.data.get("bio", user.bio)
    user.profile_image_url = request.data.get("profile_image_url", user.profile_image_url)
    user.email = request.data.get("email", user.email)
    user.active = request.data.get("active", user.active)
    user.is_staff = request.data.get("is_staff", user.is_staff)
    user.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)

    
  def destroy(self, request, pk):
        user = RareUser.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class RareUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RareUser
        fields = ['id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid']
        depth = 2
