from .models import User
from rest_framework import serializers,status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField
from django.core.validators import validate_email
import re #re is used to work with regular expressions



class UserCreationSerializer(serializers.ModelSerializer): #UserCreationSerializer is used to create a user
    username=serializers.CharField(max_length=40,allow_blank=True)
    email=serializers.EmailField(max_length=80,allow_blank=False)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
    password=serializers.CharField(allow_blank=False,write_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    birth_date = serializers.DateField(allow_null=False)
    gender = serializers.CharField(max_length=1, allow_null=True, allow_blank=True)
    first_name = serializers.CharField(max_length=30, allow_blank=True)
    last_name = serializers.CharField(max_length=30, allow_blank=True)
    address = serializers.CharField(allow_null=True, allow_blank=True)
    city = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    state = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    country = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    zip_code = serializers.CharField(max_length=20, allow_null=True, allow_blank=True)

    class Meta: #Meta class is used to define the fields that will be used when the the user signs up
        model=User
        fields=['id','username', 'email', 'phone_number','password', 'date_joined', 'birth_date', 'gender','first_name', 'last_name', 'address', 'city', 'state', 'country', 'zip_code']

    def validate_email(self, value):
        """Validate email format"""
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format.")
        return value

    def validate_phone_number(self, value):
        """Validate phone number format (example: +201002664818)"""
        phone_pattern = r'^\+?\d{10,15}$'  # Allows + and 10-15 digits
        if not re.match(phone_pattern, value):
            raise serializers.ValidationError("Invalid phone number format. Use an international format like +201002664818.")
        return value

    def validate_birth_date(self, value):
        if not value:
            raise serializers.ValidationError("Birth date is required.")
        return value

    def validate_gender(self, value):
        if value not in dict(User.GENDER_CHOICES):
            raise serializers.ValidationError("Invalid gender selection.")
        return value
    
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("E-mail is required.")
        return value
    
    def validate_phone_number(self, value):
        if not value:
            raise serializers.ValidationError("Phone Number is required.")
        return value
    

    def validate(self,attrs): #validate is used to validate the data
        email=User.objects.filter(email=attrs.get('email')).exists() #check if the email exists

        if email:
            raise ValidationError(detail="Another Health Keeper with the same E-mail already exists",code=status.HTTP_400_BAD_REQUEST) #if email exists, raise an error

        username=User.objects.filter(username=attrs.get('username')).exists() #check if the username exists

        if username: #if username exists
            raise ValidationError(detail="Another Health Keeper with the same username already exists",code=status.HTTP_400_BAD_REQUEST) #raise an error
        
        phone_number=User.objects.filter(phone_number=attrs.get('phone_number')).exists() #check if the phone number exists
        if phone_number: #if phone number exists
            raise ValidationError(detail="Another Health Keeper with the same phone number already exists",code=status.HTTP_400_BAD_REQUEST) #raise an error


        return super().validate(attrs)


    def create(self,validated_data): #create is used to create a user
        new_user=User(**validated_data) #create a new user

        new_user.password=make_password(validated_data.get('password')) #set the password of the user

        new_user.save()

        return new_user
