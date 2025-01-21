from .models import User
from rest_framework import serializers,status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer): #UserCreationSerializer is used to create a user
    username=serializers.CharField(max_length=40,allow_blank=True)
    email=serializers.EmailField(max_length=80,allow_blank=False)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
    password=serializers.CharField(allow_blank=False,write_only=True)


    class Meta: #Meta class is used to define the model and fields
        model=User
        fields=['id','username', 'email', 'phone_number','password']

    def validate(self,attrs): #validate is used to validate the data
        email=User.objects.filter(username=attrs.get('username')).exists() #check if the email exists

        if email:
            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN) #if email exists, raise an error

        username=User.objects.filter(username=attrs.get('username')).exists() #check if the username exists

        if username: #if username exists
            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN) #raise an error

        return super().validate(attrs)


    def create(self,validated_data): #create is used to create a user
        new_user=User(**validated_data) #create a new user

        new_user.password=make_password(validated_data.get('password')) #set the password of the user

        new_user.save()

        return new_user
