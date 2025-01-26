from django.db import models 
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import AbstractUser #AbstractUser is used to create a custom user model
from phonenumber_field.modelfields import PhoneNumberField #PhoneNumberField is used to store the phone number of the user
from django.utils import timezone
import datetime





class CustomUserManager(BaseUserManager): 
    def create_user(self,email,password,**extra_fields): 
        if not email: #if email is not provided
            raise ValueError(_('Please enter a valid E-mail address'))

        email=self.normalize_email(email) #normalize_email is used to convert the email to lowercase

        new_user=self.model(email=email,**extra_fields) #create a new user

        new_user.set_password(password) #set the password of the user

        new_user.save()

        return new_user


    def create_superuser(self,email,password,**extra_fields): 

        extra_fields.setdefault('is_superuser',True) #set is_superuser to True
        extra_fields.setdefault('is_staff',True) #set is_staff to True
        extra_fields.setdefault('is_active',True) #set is_active to True

        if extra_fields.get('is_superuser') is not True: #if is_superuser is not True
            raise ValueError(_('Admin should have is_superuser=True'))

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Auditor should have is_staff=True'))


        return self.create_user(email,password,**extra_fields)


class User(AbstractUser): #User is used to create a custom user model
    GENDER_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    ]
    username=models.CharField(_('username'), max_length=40, unique=True)
    email=models.EmailField(_('Email'), max_length=80,unique=True, null=False, blank=False)
    phone_number=PhoneNumberField(unique=True,null=False,blank=False)
    date_joined=models.DateTimeField(_('Date'),auto_now_add=True)
    birth_date = models.DateField(_('Birth Date'), null=False, default=datetime.date.today)
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    address = models.TextField(_('Address'), blank=True, null=True)
    city = models.CharField(_('City'), max_length=50, blank=True, null=True)
    state = models.CharField(_('State'), max_length=50, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=50, blank=True, null=True)
    zip_code = models.CharField(_('ZIP Code'), max_length=20, blank=True, null=True)


    REQUIRED_FIELDS=['email', 'phone_number','password','birth_date' ] #REQUIRED_FIELDS is used to specify the fields that are required to create a user
    USERNAME_FIELD='username' #USERNAME_FIELD is used to specify the field that is used as the username

    def __str__(self):
        return f"User {self.username}" #return the username of the user
