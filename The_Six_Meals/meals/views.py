from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import Meal
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema


user=get_user_model()

class HelloAuthView(View): 
    @swagger_auto_schema(operation_summary="Welcome to the health keeper service")
    def get(self, request):
        return HttpResponse("Hello, Authenticated Health Keeper!")

class MealView(View):
    def get(self, request):
        return HttpResponse('This is the Meal View')
    
class MealCreateListView(generics.GenericAPIView): 
    serializer_class = serializers.MealCreationSerializer
    queryset = Meal.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(operation_summary="List all meals made by the health keeper")
    def get(self, request): 
        meals = Meal.objects.all()
        serializer = self.serializer_class(instance=meals, many=True)
        return Response(data={"message": "Welcome to the meal creation page for the Health Keeper", "meals": serializer.data}, status=status.HTTP_200_OK)
    @swagger_auto_schema(operation_summary="Create a new meal for the Health Keeper")
    def post(self, request): 
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class MealDetailView(generics.GenericAPIView): 
    serializer_class = serializers.MealDetailSerializer
    permission_classes = [IsAdminUser] 
    @swagger_auto_schema(operation_summary="Get a meal detail by its ID")
    def get(self, _, meal_id):
        meal = get_object_or_404(Meal,pk=meal_id)
        serializer=self.serializer_class(instance=meal)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Update a meal by its ID")
    def put(self, request, meal_id): 
        data = request.data
        meal = get_object_or_404(Meal, pk=meal_id)
        serializer = self.serializer_class(data=data, instance=meal, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(operation_summary="Delete a meal by its ID")
    def delete(self, _, meal_id): 
        meal=get_object_or_404(Meal,pk=meal_id)
        meal.delete()
        return Response(data={"message": "Meal deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class UpdateMealStatus(generics.GenericAPIView): 
    serializer_class= serializers.MealStatusUpdateSerializer
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(operation_summary="Update a meal status by its ID")
    def put (self, request,meal_id): 
        meal=get_object_or_404(Meal,pk=meal_id)

        data=request.data

        serializer=self.serializer_class(data=data, instance=meal)

        if serializer.is_valid(): 
            serializer.save() 
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserMealView(generics.GenericAPIView):  
    serializer_class = serializers.MealDetailSerializer

    @swagger_auto_schema(operation_summary="Get all meals made by the health keeper")
    def get(self, request, user_id):
        User = get_user_model()  
        requested_user = get_object_or_404(User, pk=user_id) 
        meals = Meal.objects.filter(customer=requested_user)  
        serializer = self.serializer_class(instance=meals, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class UserMealDetail(generics.GenericAPIView): 
    serializer_class = serializers.MealDetailSerializer

    @swagger_auto_schema(operation_summary="Get a meal detail made by specific Health Keeper")
    def get(self, request, user_id, meal_id):
        User = get_user_model()  
        requested_user = get_object_or_404(User, pk=user_id) 
        meal = get_object_or_404(Meal, pk=meal_id, customer=requested_user) 
        serializer = self.serializer_class(instance=meal)
        return Response(data=serializer.data, status=status.HTTP_200_OK)