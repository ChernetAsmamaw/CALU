from django.urls import path
from .views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('profiles/', UserProfileList.as_view()),   
    path('profiles/<int:pk>/', UserProfileDetail.as_view())
]