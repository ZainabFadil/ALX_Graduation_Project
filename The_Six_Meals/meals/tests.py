from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from meals.models import Meal  


User = get_user_model()  


class MealViewsTests(APITestCase):
    def setUp(self):
        """
        Setup the test environment by creating a user and meals.
        """
        self.client = APIClient()
        self.url = '/meal/meals/'
        self.user = User.objects.create_user(
            first_name='Mahmoud',
            last_name='Ali',
            address='Ehorya street',
            city='Cairo',
            state='New Cairo',
            country='Egypt',
            zip_code='4710001',
            email='mahmoud.elsharawy10@gmail.com',
            password='CNX@134tb',
            username='mahmoudali',
            phone_number='+201002665599',
            birth_date='1990-01-01',
            gender='M'
        )

        self.client.force_authenticate(user=self.user)

        self.meal_data = {
            'meal_name': 'Salad',
            'types': 'BREAKFAST',
            'meal_status': 'PENDING',
            'fats_in_grams': 0,
            'meal_choices': 'VEGAN',
            'description': 'Salad is very healthy',
            'Ingredients': 'Ingredients',
            'Recipe': 'Recipe',
            'vitamins': 'Vitamin A, Vitamin C',
            'minerals': 'Iron, Calcium',
            'calories': 100,
            'proteins_in_grams': 10,
            'carbohydrates_in_grams': 80,
        }
        self.meal = Meal.objects.create(customer=self.user, **self.meal_data)

        
        self.create_meal_url = reverse('create_meal')  # Adjust based on your URL name
        self.meal_detail_url = reverse('meal_detail', kwargs={'meal_id': self.meal.id})
        self.user_meal_url = reverse('users_meals', kwargs={'user_id': self.user.id})
        self.user_meal_detail_url = reverse('user_specific_meals', kwargs={'user_id': self.user.id, 'meal_id': self.meal.id})


    def test_hello_auth_view(self):
        response = self.client.get(reverse('hello_health_keeper'))  # Adjust based on your URL name
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Hello, Authenticated Health Keeper!")

    def test_meal_create_list_view(self):

        response = self.client.get(self.create_meal_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('meals', response.data)


        response = self.client.post(self.create_meal_url, self.meal_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['meal_name'], self.meal_data['meal_name'])

    def test_meal_detail_view(self):

        admin_user = User.objects.create_superuser(
            email="soha@appe.com", password="vbh@cfg123", username="sohaadmin"
        )
        self.client.force_authenticate(user=admin_user)

        response = self.client.get(self.meal_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['meal_name'], self.meal_data['meal_name'])

    def test_update_meal_status_view(self):

        admin_user = User.objects.create_superuser(
            email="samir@example.com", password="addsmjf5123", username="samirsaad"
        )
        self.client.force_authenticate(user=admin_user)
        self.meal = Meal.objects.create(
            customer=self.user,
            meal_name="fruit salad",
            types="BREAKFAST",
            meal_status="PENDING",
            fats_in_grams=0,
            meal_choices="VEGAN",
            description="Fruit salad is very healthy",
            Ingredients="Ingredients",
            Recipe="Recipe",
            vitamins="Vitamin A, Vitamin C",
            minerals="Iron, Calcium",
            calories=100,
            proteins_in_grams=10,
            carbohydrates_in_grams=80,
        )

   
        self.url = reverse('update_meal_status', kwargs={'meal_id': self.meal.id})


        updated_data = {'meal_status': 'COMPLETED'}
        response = self.client.put(self.url, updated_data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)


        self.meal.refresh_from_db()
        self.assertEqual(self.meal.meal_status, 'COMPLETED')



    def test_user_meal_view(self):

        response = self.client.get(self.user_meal_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['meal_name'], self.meal_data['meal_name'])

    def test_user_meal_detail_view(self):

        response = self.client.get(self.user_meal_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['meal_name'], self.meal_data['meal_name'])

    def test_delete_meal(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
        email="saber@app.com", password="BNR#4f123", username="saberahemd"
           )

        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(self.meal_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Meal.objects.count(), 0)

    def test_meal_create_without_login(self):

        self.client.logout()


        response = self.client.post(self.create_meal_url, self.meal_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_create_user_meal_choices_failure(self):

        self.invalid_meal_choices_data = {
        'meal_name': 'Pasta Primavera',
        'types': 'Brunch', 
        'ingredients': 'Pasta, tomatoes, garlic, cream',
        'calories': 500,
        'meal_time': '12:00',
        'meal_choice': 'fresh',  
        'health_keeper': 'mahmoudali',  
    }


        response = self.client.post(self.url, self.invalid_meal_choices_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_meal_types_failure(self):

        self.invalid_meal_types_data = {
        'meal_name': 'Pasta Primavera',
        'types': 'desserts',  
        'ingredients': 'Pasta, tomatoes, garlic, cream',
        'calories': 500,
        'meal_time': '12:00',
        'meal_choice': 'VEGAN',
        'health_keeper': 'mahmoudali', 
    }


        response = self.client.post(self.url, self.invalid_meal_types_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_meal_status_failure(self):

        self.invalid_meal_status_data = {
        'meal_name': 'Pasta Primavera',
        'types': 'BREAKFAST',  
        'ingredients': 'Pasta, tomatoes, garlic, cream',
        'calories': 500,
        'meal_time': '12:00',
        'meal_choice': 'VEGAN',
        'meal_status': 'READY', 
        'health_keeper': 'mahmoudali', 
    }


        response = self.client.post(self.url, self.invalid_meal_status_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(User.objects.count(), 1)

    