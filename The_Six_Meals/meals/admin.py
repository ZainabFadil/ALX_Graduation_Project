# Django Admin Configuration for Meal Model
# -------------------------------------------
# This file registers the Meal model with the Django admin interface, allowing 
# easy management of meals from the Django admin panel. It defines custom 
# configurations for displaying and filtering the Meal model data, including 
# the fields to display in the list view, filters for narrowing down the list, 
# and search functionality to find meals by name, status, or type.

from django.contrib import admin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin): #MealAdmin is used to register the Meal model
    list_display = ['meal_name', 'types', 'meal_status', 'created_at', 'updated_at'] #list_display is used to display the fields in the admin panel
    list_filter = ['created_at', 'updated_at', 'types', 'meal_status'] #list_filter is used to filter the fields
    search_fields = ['meal_name', 'meal_status', 'types'] #search_fields is used to search the fields
   