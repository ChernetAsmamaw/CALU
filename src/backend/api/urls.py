from django.urls import path
from .views import UserProfileList, UserProfileDetail   
from drf_yasg.views import get_schema_view
from drf_yasg import openapi   
from rest_framework.schemas import get_schema_view as rest_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="User Profile API",
        default_version='v1',
        description="API for user profiles",      
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),           
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),          
)

def api_root(request, format=None):
    return rest_schema_view(
        title='User Profile API',        
        patterns=[urlpatterns]
    )(request, format)

urlpatterns = [
    path('api/', api_root),
    path('profiles/', UserProfileList.as_view()),        
    path('profiles/<int:pk>/', UserProfileDetail.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs.json/', schema_view.without_ui(cache_timeout=0), name='schema-json')   
]