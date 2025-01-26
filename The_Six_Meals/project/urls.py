from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from meals import views
from django.urls import path
from rest_framework.permissions import AllowAny
from django.urls import path

schema_view = get_schema_view(
   openapi.Info(
      title="The Six Meals API",
      default_version='v1',
      description="A simple Django Rest Framework API for the health keepers service",
      contact=openapi.Contact(email="amlnasser@app.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('meal/', include('meals.urls')),
    path('swagger<format>.json|.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0)),
    path('', views.HelloAuthView.as_view(), name='hello_health_keeper'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/jwt/verify/', TokenVerifyView.as_view(), name='token_verify')
    
]