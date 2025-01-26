from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.UserSerializer.as_view(),name='sign_up_for_a_new_Health_Keeper'), #signup is used to create a new user
] 