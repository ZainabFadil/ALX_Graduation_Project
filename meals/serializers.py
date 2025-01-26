from rest_framework import serializers
from .models import Meal
from rest_framework.views import APIView

class MealCreationSerializer(serializers.ModelSerializer): #MealCreationSerializer is used to create a meal
    meal_name = serializers.CharField(default='Healthy Meal')
    type = serializers.CharField(default='BREAKFAST')
    meal_choices = serializers.CharField(default='VEGAN')
    meal_status = serializers.CharField(default='PENDING')
    description = serializers.CharField(default='Description')
    Ingredients = serializers.CharField(default='Ingredients')
    Recipe = serializers.CharField(default='Recipe')
    vitamins = serializers.CharField(default='Vitamins')
    minerals = serializers.CharField(default='Minerals')
    calories = serializers.IntegerField(required=False, default=0)
    proteins_in_grams = serializers.IntegerField(required=False, default=0)
    fats_in_grams = serializers.IntegerField(required=False, default=0)
    carbohydrates_in_grams = serializers.IntegerField(required=False, default=0)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Meal
        fields = ['id','meal_name', 'type', 'meal_status','created_at', 'updated_at', 'fats_in_grams', 'meal_choices', 'description', 'Ingredients', 'Recipe', 'vitamins', 'minerals', 'calories', 'proteins_in_grams', 'fats_in_grams', 'carbohydrates_in_grams', 'created_at', 'updated_at', 'customer']

class MealDetailSerializer(serializers.ModelSerializer): #MealDetailSerializer is used to display the meal details
    meal_name = serializers.CharField(default='Healthy Meal')
    type = serializers.CharField(default='BREAKFAST')
    meal_choices = serializers.CharField(default='VEGAN')
    meal_status = serializers.CharField(default='PENDING')
    description = serializers.CharField(default='Description')
    Ingredients = serializers.CharField(default='Ingredients')
    Recipe = serializers.CharField(default='Recipe')
    vitamins = serializers.CharField(default='Vitamins')
    minerals = serializers.CharField(default='Minerals')
    calories = serializers.IntegerField(required=False, default=0)
    proteins_in_grams = serializers.IntegerField(required=False, default=0)
    fats_in_grams = serializers.IntegerField(required=False, default=0)
    carbohydrates_in_grams = serializers.IntegerField(required=False, default=0)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    customer = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Meal
        fields = ['id','meal_name', 'type', 'meal_status','created_at', 'updated_at', 'fats_in_grams', 'meal_choices', 'description', 'Ingredients', 'Recipe', 'vitamins', 'minerals', 'calories', 'proteins_in_grams', 'fats_in_grams', 'carbohydrates_in_grams', 'created_at', 'updated_at', 'customer']
        

class MealStatusUpdateSerializer(serializers.ModelSerializer): #MealStatusUpdateSerializer is used to update the meal status
    
    meal_status=serializers.CharField(default='PENDING')

    class Meta: #Meta class is used to define the model and fields
        model=Meal
        fields = ['meal_status']