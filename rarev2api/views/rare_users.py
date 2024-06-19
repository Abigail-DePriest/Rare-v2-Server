from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import RareUsers

class RareUserView(ViewSet):
  def retrieve(self, request, pk):
        try:
            user = RareUsers.objects.get(pk=pk)
            serializer = RareUserSerializer(user)
            return Response(serializer.data)
        except RareUsers.DoesNotExist:
            return Response({'message': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
          
  def list(self, request):
        users = RareUsers.objects.all()
               
        serializer = RareUserSerializer(users, many=True)
        return Response(serializer.data)       
  
  def create(self, request):
   
    user = RareUsers.objects.create(
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
        user = RareUsers.objects.get(pk=pk)
    except RareUsers.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user.first_name = request.data["first_name"]
    user.last_name = request.data["last_name"]
    user.bio = request.data["bio"]
    user.profile_image_url = request.data["profile_image_url"]
    user.email = request.data["email"]
    user.active = request.data.get("active", user.active)
    user.is_staff = request.data.get("is_staff", user.is_staff)
    user.uid = request.data["uid"]
    user.save()

    return Response(None, status=status.HTTP_204_NO_CONTENT)

    
  def destroy(self, request, pk):
        user = RareUsers.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

class RareUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RareUsers
        fields = ['id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid']
        depth = 2
