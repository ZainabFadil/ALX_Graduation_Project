# Django App Configuration for Meals App
# ---------------------------------------
# This file contains the configuration for the 'meals' app. The MealsConfig 
# class inherits from AppConfig and defines the app's name and default auto 
# django.apps is a module that provides a registry of installed applications.


from django.apps import AppConfig

class MealsConfig(AppConfig): #MealsConfig is used to configure the meals app
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meals'
    
