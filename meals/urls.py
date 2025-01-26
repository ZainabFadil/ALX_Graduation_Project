from django.urls import path
from . import views
from meals.views import HelloAuthView
from meals.views import MealView
urlpatterns = [
    path('meal/<int:meal_id>/', views.MealDetailView.as_view(), name='meal_detail'),
    path('meals', views.MealCreateListView.as_view(), name='create_meal'),
    path('update-status/<int:meal_id>/', views.UpdateMealStatus.as_view(), name='update_meal_status'),
    path('user/<int:user_id>/meals/', views.UserMealView.as_view(), name='users_meals'),
    path('hello/', HelloAuthView.as_view(), name='hello_auth'),
    path('user/<int:user_id>/meals/<int:meal_id>/', views.UserMealDetail.as_view(), name='user_specific_meals'),
] 
