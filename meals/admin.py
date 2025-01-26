from django.contrib import admin
from .models import Meal

# Register your models here.

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin): #MealAdmin is used to register the Meal model
    list_display = ['meal_name', 'type', 'meal_status', 'created_at', 'updated_at'] #list_display is used to display the fields in the admin panel
    list_filter = ['created_at', 'updated_at', 'type', 'meal_status'] #list_filter is used to filter the fields
    search_fields = ['meal_name', 'meal_status', 'type'] #search_fields is used to search the fields
   