# Django Authentication and URL Configuration
# ---------------------------------------------
# This file contains the routing and authentication logic for the application.
# It defines the URL patterns for user login, registration, and authentication 
# views. It also includes URL path configurations to secure endpoints and manage 
# access control for various views. 
#
# Ensure to update this file whenever there are changes to authentication methods 
# or when adding new secure endpoints.

from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.UserSerializer.as_view(),name='sign_up_for_a_new_Health_Keeper'), #signup is used to create a new user
] 