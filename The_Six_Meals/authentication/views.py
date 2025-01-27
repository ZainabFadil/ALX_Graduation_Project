# Django Authentication Views
# -----------------------------
# This file contains views related to user authentication, specifically 
# for user creation (sign-up). It uses Django REST Framework (DRF) to 
# handle the creation of new users through a POST request. The views 
# validate the data using serializers and return appropriate response 
# statuses based on the result (success or failure).

from django.shortcuts import render
from .models import User
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

class UserSerializer(generics.GenericAPIView): #UserSerializer is used to create a user
    serializer_class=serializers.UserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a new Health Keeper account by signing Up") #swagger_auto_schema is used to create a schema for the API
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid(): #if the serializer is valid
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED) #return the data and status code

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST) #return the errors and status code