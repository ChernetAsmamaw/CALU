from rest_framework import generics, permissions, filters
from .serializers import UserProfileSerializer  
from .models import UserProfile
from .permissions import IsOwnerOrReadOnly

class UserProfileList(generics.ListCreateAPIView):
    
    queryset = UserProfile.objects.all()    
    serializer_class = UserProfileSerializer
    
    filter_backends = [filters.SearchFilter]  
    search_fields = ['name', 'username']
      
    ordering_fields = ['name', 'username']
    

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
      
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
      
    permission_classes = [IsOwnerOrReadOnly]