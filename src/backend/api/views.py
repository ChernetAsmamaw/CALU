from rest_framework import generics
from .serializers import UserProfileSerializer  
from .models import UserProfile
from .permissions import IsOwnerOrReadOnly

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]