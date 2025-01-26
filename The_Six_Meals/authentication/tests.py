from rest_framework.test import APITestCase
from rest_framework import status #status is used to check the status of the response
from django.urls import reverse 
from django.contrib.auth import get_user_model
import datetime
from phonenumber_field.phonenumber import PhoneNumber


User = get_user_model()




class UserSerializerTests(APITestCase):
    def setUp(self):
        self.url = reverse('sign_up_for_a_new_Health_Keeper')
        self.valid_data = {
            'first_name': 'Mahmoud',
            'last_name': 'Ali',
            'address': 'Ehorya street',
            'city': 'Cairo',
            'state': 'New Cairo',
            'country': 'Egypt',
            'zip_code': '4710001',
            'email': 'mahmoud.elsharawy10@gmail.com',  
            'password': 'CNX@134tb',
            'username': 'mahmoudali',
            'phone_number': '+201002665599',
            'birth_date': '1990-01-01',
            'gender': 'M'
        
        }
        
    def test_create_user_success(self):
        response = self.client.post(self.url, self.valid_data, format='json')

        
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       
       
        self.assertEqual(User.objects.count(), 1)

    
    def test_create_user_email_failure(self):
        self.invalid_email = {
            'first_name': 'Ramy',
            'last_name': 'Saad',
            'address': '18th street',
            'city': 'Giza',
            'state': 'Elharam',
            'country': 'Egypt',
            'zip_code': '4710001',
            'email': 'Hi@app',  # Invalid email
            'password': 'CvB@45fgb',
            'username': 'ahmoudali',
            'phone_number': '+201002664830',
            'birth_date': datetime.date(1990, 1, 1),
            'gender': 'M'
        }

        # Test that creating a user with invalid email returns a bad request
        response = self.client.post(self.url, self.invalid_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Ensure no user was created
        self.assertEqual(User.objects.count(), 0)


    def test_create_user_duplicate_email(self):
        # Create an initial user
        self.client.post(self.url, self.valid_data, format='json')

        self.duplicate_email = {
            'first_name': 'Saber',
           'last_name': 'Selim',
           'address': 'Ehorya street',
           'city': 'Cairo',
           'state': 'New Cairo',
           'country': 'Egypt',
           'zip_code': '4710001',
           'email': 'mahmoud.elsharawy10@gmail.com',  # Duplicate email
           'password': 'Non34mfkg',
           'username': 'saberselim',
           'phone_number': '+201002668790',
           'birth_date': datetime.date(1990, 1, 1),
           'gender': 'M'
       }

    
        """
        Test creating a user with a duplicate email should return HTTP 400 Bad Request.
        """
        # Attempt to create a user with a duplicate email
        response = self.client.post(self.url, self.duplicate_email, format='json')
        
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Assert that no new user is created, only the original user should exist
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_duplicate_username(self):
        # Create an initial user
        self.client.post(self.url, self.valid_data, format='json')
        # Attempt to create a user with a duplicate username
        self.duplicate_username = {
            'first_name': 'Samir',
           'last_name': 'Samra',
           'address': 'Ehorya street',
           'city': 'Cairo',
           'state': 'New Cairo',
           'country': 'Egypt',
           'zip_code': '4710001',
           'email': 'eman.elsharawy10@gmail.com',  
           'password': 'Non34mfkg',
           'username': 'mahmoudali', # Duplicate username
           'phone_number': '+201002668790',
           'birth_date': datetime.date(1990, 1, 1),
           'gender': 'M'
       }

    
        """
        Test creating a user with a duplicate email should return HTTP 400 Bad Request.
        """
        # Attempt to create a user with a duplicate username
        response = self.client.post(self.url, self.duplicate_username, format='json')
        
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Assert that no new user is created, only the original user should exist
        self.assertEqual(User.objects.count(), 1)
    
    def test_create_user_duplicate_phone_number(self):
        # Create an initial user
        self.client.post(self.url, self.valid_data, format='json')
        # Attempt to create a user with a duplicate phone number
        self.duplicate_phone_number = {
            'first_name': 'Serine',
           'last_name': 'ahmed',
           'address': 'Ehorya street',
           'city': 'Cairo',
           'state': 'New Cairo',
           'country': 'Egypt',
           'zip_code': '4710001',
           'email': 'serin@app.com',  
           'password': 'Non34mfkg',
           'username': 'serinahmed',
           'phone_number': '+201002665599', # Duplicate phone number
           'birth_date': datetime.date(1990, 1, 1),
           'gender': 'M'
       }

    
        """
        Test creating a user with a duplicate email should return HTTP 400 Bad Request.
        """
        # Attempt to create a user with a duplicate phone number
        response = self.client.post(self.url, self.duplicate_phone_number, format='json')
        
        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Assert that no new user is created, only the original user should exist
        self.assertEqual(User.objects.count(), 1)
    
    def test_create_user_gender_failure(self):
        self.invalid_gender_selection_data = {
            'first_name': 'Sameh',
            'last_name': 'Mohamed',
            'address': '15th street',
            'city': 'Giza',
            'state': 'Elharam',
            'country': 'Egypt',
            'zip_code': '4710001',
            'email': 'aml.elsharawy31@gmail.com',  
            'password': 'CvB@45fgb',
            'username': 'ahmoudali',
            'phone_number': '+201002664818',
            'birth_date': datetime.date(1990, 1, 1),
            'gender': 'S'  # Invalid
        }

        # Test that creating a user with invalid gender selection returns a bad request
        response = self.client.post(self.url, self.invalid_gender_selection_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Ensure no user was created
        self.assertEqual(User.objects.count(), 0)

    def test_create_user_birth_date_failure(self):
        self.blank_birth_date_data = {
            'first_name': 'Sameh',
            'last_name': 'Mohamed',
            'address': '15th street',
            'city': 'Giza',
            'state': 'Elharam',
            'country': 'Egypt',
            'zip_code': '4710001',
            'email': 'amlnasser500@gmail.com',  
            'password': 'CvB@45fgb',
            'username': 'samehsameh',
            'phone_number': '+201002664818',
            'birth_date': '',  #blank
            'gender': 'M' 
        }

        # Test that creating a user with blank Birth Date returns a bad request
        response = self.client.post(self.url, self.blank_birth_date_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Ensure no user was created
        self.assertEqual(User.objects.count(), 0)

    def test_create_user_with_blank_phone_number_failure(self):
        self.blank_phone_number_data = {
            'first_name': 'Sameh',
            'last_name': 'Mohamed',
            'address': '15th street',
            'city': 'Giza',
            'state': 'Elharam',
            'country': 'Egypt',
            'zip_code': '4710001',
            'email': 'nasser500@app.com',  
            'password': 'CvB@45fgb',
            'username': 'samehali',
            'phone_number': '', #blank
            'birth_date': datetime.date(1990, 1, 1),  
            'gender': 'M' 
        }

        # Test that creating a user with blank phone number returns a bad request
        response = self.client.post(self.url, self.blank_phone_number_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Ensure no user was created
        self.assertEqual(User.objects.count(), 0)

    def test_create_user_with_blank_email_failure(self):
        self.blank_email_data = {
            'first_name': 'Sameh',
            'last_name': 'Mohamed',
            'address': '15th street',
            'city': 'Giza',
            'state': 'Elharam',
            'country': 'Egypt',
            'zip_code': '4710001',
            'email': '', #blank 
            'password': 'CvB@45fgb',
            'username': 'samehali',
            'phone_number': '+201003331980', 
            'birth_date': datetime.date(1990, 1, 1),  
            'gender': 'M' 
        }

        # Test that creating a user with blank E-mail address returns a bad request
        response = self.client.post(self.url, self.blank_email_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Ensure no user was created
        self.assertEqual(User.objects.count(), 0)

    def test_create_user_with_invalid_phone_number_failure(self):
        self.invalid_phone_number = {
            'first_name': 'Rahim',
            'last_name': 'Mohamed',
            'address': '15th street',
            'city': 'Giza',
            'state': 'Elharam',
            'country': 'Egypt',
            'zip_code': '4710001',
            'email': 'hopeinlife@app.com', 
            'password': 'CvB@45fgb',
            'username': 'rahimmohamed',
            'phone_number': '+201033', #invalid phone number
            'birth_date': datetime.date(1990, 1, 1),  
            'gender': 'M' 
        }

        # Test that creating a user with invalid phone number format returns a bad request
        response = self.client.post(self.url, self.invalid_phone_number, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Ensure no user was created
        self.assertEqual(User.objects.count(), 0)

      
