from django.db import models 
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ #gettext_lazy is used to translate the string to the language of the user
from django.contrib.auth.models import AbstractUser #AbstractUser is used to create a custom user model
from phonenumber_field.modelfields import PhoneNumberField #PhoneNumberField is used to store the phone number of the user



class CustomUserManager(BaseUserManager): #CustomUserManager is used to create a custom user manager
    def create_user(self,email,password,**extra_fields): #create_user is used to create a user
        if not email: #if email is not provided
            raise ValueError(_('Please enter an email address'))

        email=self.normalize_email(email) #normalize_email is used to convert the email to lowercase

        new_user=self.model(email=email,**extra_fields) #create a new user

        new_user.set_password(password) #set the password of the user

        new_user.save()

        return new_user


    def create_superuser(self,email,password,**extra_fields): #create_superuser is used to create a superuser

        extra_fields.setdefault('is_superuser',True) #set is_superuser to True
        extra_fields.setdefault('is_staff',True) #set is_staff to True
        extra_fields.setdefault('is_active',True) #set is_active to True

        if extra_fields.get('is_superuser') is not True: #if is_superuser is not True
            raise ValueError(_('Superuser must have is_superuser=True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))


        return self.create_user(email,password,**extra_fields)


class User(AbstractUser): #User is a custom user model
    username=models.CharField(_('Username'), max_length=40,unique=True)
    email=models.CharField(_('Email'), max_length=80,unique=True)
    phone_number=PhoneNumberField(unique=True,null=False,blank=False)
    date_joined=models.DateTimeField(_('Date'),auto_now_add=True)


    REQUIRED_FIELDS=['username','phone_number']
    USERNAME_FIELD='email'

    def __str__(self):
        return f"User {self.username}"
