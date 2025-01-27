# Django Model for Meal
# -----------------------
# This file defines the Meal model, which stores details about different 
# types of meals, including their names, types (e.g., breakfast, lunch), 
# dietary choices (e.g., vegan, gluten-free), meal status (e.g., pending, 
# completed), nutritional information (e.g., calories, proteins, fats), 
# and other relevant details such as ingredients and recipe. 
# The model also has a foreign key relationship with the User model, 
# associating each meal with a specific user.

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Meal(models.Model): #Meal is a model to store the meal details
    TYPES = (
        ('BREAKFAST', 'breakfast'),
        ('BRUNCH', 'brunch'),
        ('SNACK', 'snack'),
        ('LUNCH', 'lunch'),
        ('DINNER', 'dinner'),
        ('SUPPER', 'supper')
    )
    MEAL_CHOICES = (
        ('VEGAN', 'vegan'),
        ('VEGETARIAN', 'vegetarian'),
        ('PALEO', 'paleo'),
        ('KETO', 'keto'),
        ('GLUTEN_FREE', 'gluten free'),
        ('DAIRY_FREE', 'dairy free'),
        ('NUT_FREE', 'nut free'),
        ('SHELLFISH_FREE', 'shellfish free'),
        ('SOY_FREE', 'soy free'),
        ('WHEAT_FREE', 'wheat free'),
        ('EGG_FREE', 'egg free'),
        ('FISH_FREE', 'fish free'),
        ('NO_RESTRICTIONS', 'no restrictions')
    )
    MEAL_STATUS = (
        ('PENDING', 'pending'),
        ('COMPLETED', 'completed'),
        ('CANCELLED', 'cancelled')
    )

    meal_name = models.CharField(max_length=200, default='Healthy Meal')
    types = models.CharField(max_length=80, choices=TYPES, default='BREAKFAST')
    meal_choices = models.CharField(max_length=300, choices=MEAL_CHOICES, blank=True, default='VEGAN')
    meal_status = models.CharField(max_length=80, choices=MEAL_STATUS, default=MEAL_STATUS[0][0])
    description = models.CharField(max_length=1000, default='Description')
    Ingredients = models.CharField(max_length=1000, default='Ingredients')
    Recipe = models.CharField(max_length=1000, default='Recipe')
    vitamins = models.CharField(max_length=1000, default='Vitamins')
    minerals = models.CharField(max_length=1000, default='Minerals')
    calories = models.IntegerField(null=True, blank=True, default=0)
    proteins_in_grams = models.IntegerField(null=True, blank=True, default=0)
    fats_in_grams = models.IntegerField(null=True, blank=True, default=0)
    carbohydrates_in_grams = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals', null=True, blank=True)
    def __str__(self): #__str__ is used to return the string representation of the object
        return f"<Meal {self.meal_name} ({self.types})>"