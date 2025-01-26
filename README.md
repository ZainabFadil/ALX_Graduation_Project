# Graduation Project

**The Six Meals App:**
Our app provides six balanced meals within the day to ensure that you get all the nourishment that you need to stay energetic and to keep a healthy diet and routine.

1. **Breakfast**

   - **Time:** Morning
   - **Identity:** A traditional, hearty meal that provides energy and nourishment to kickstart the day. It’s perfect for those who enjoy a fulfilling and comforting start to their morning.
   - **Ideal for:** Individuals who want a balanced meal that fuels their day with essential nutrients and familiar flavors.
   - **Example:** Scrambled eggs with whole-grain toast and avocado, or a warm bowl of oatmeal with nuts and honey.

2. **Brunch**

   - **Time:** Late morning
   - **Identity:** A high-protein meal designed for those who need a strong boost of energy after morning activities, workouts, or late risers who prefer a more filling meal instead of breakfast.
   - **Ideal for:** Athletes, fitness enthusiasts, or anyone needing protein-rich nourishment to stay full and energized.
   - **Example:** Grilled chicken with quinoa and roasted vegetables, or a protein smoothie with almond butter and spinach.

3. **Lunch**

   - **Time:** Around noon
   - **Identity:** A plant-based meal filled with fresh ingredients, packed with vitamins and minerals, providing a light yet fulfilling option for lunchtime.
   - **Ideal for:** Vegans, vegetarians, or anyone looking to enjoy a nutritious, plant-based meal that fuels the body without feeling heavy.
   - **Example:** A chickpea salad wrap with avocado, or a tofu stir-fry with brown rice and vegetables.

4. **Snack**

   - **Time:** Late afternoon (between lunch and dinner)
   - **Identity:** A light meal designed to keep energy levels stable and prevent overeating at dinner. Quick, healthy, and perfect for people on the go.
   - **Ideal for:** Busy individuals, students, or professionals who need a quick but nutritious bite before their evening activities.
   - **Example:** A fruit and nut smoothie, a granola bar, or a handful of mixed nuts and yogurt.

5. **Dinner**

   - **Time:** Evening
   - **Identity:** A nutrient-dense, low-carb meal designed to provide satisfaction without the heaviness of carbs, making it ideal for a balanced evening meal.
   - **Ideal for:** Those managing their weight, following a keto/low-carb diet, or wanting a healthy and fulfilling dinner option.
   - **Example:** Grilled salmon with roasted vegetables, or a fresh chicken Caesar salad without croutons.

6. **Supper**
   - **Time:** Late evening (before bed, often a lighter meal)
   - **Identity:** A comforting, family-style meal that encourages sharing and enjoying good food together. This meal balances nutrition with the joy of gathering around a table.
   - **Ideal for:** Families or groups looking for a wholesome, flavorful meal to end the day.
   - **Example:** A large pasta dish with salad, or a roasted chicken with potatoes and steamed vegetables.

This structured meal plan ensures that every part of the day is covered with a meal that aligns with your nutritional needs, lifestyle, and eating habits.

## The project is about the implementation of a simple web application that allows users to create, read, update, and delete (CRUD) notes.

**The application will be implemented using the Django Rest framework.**

**Users Overview:**

The Users App allows users to manage their personal information, including phone number, birth date, gender, and address details. It extends the built-in Django AbstractUser class and includes a custom user manager for handling user creation and superuser creation.

**Features for Users:**

**Custom User Model:**
**Purpose:** Extends AbstractUser to include additional fields.
**How it works:** Adds fields such as phone number, birth date, gender, and address details to the user model.
**Example:** A user can update their profile to include their phone number and address.

**Custom User Manager:**
**Purpose:** Implements methods for creating regular users and superusers.
**How it works:** Provides methods like `create_user` and `create_superuser` to handle user creation.
**Example:** When a new user signs up, the `create_user` method is called to create their account.

**Phone Number Support:**
**Purpose:** Stores users' phone numbers.
**How it works:** Uses `PhoneNumberField` to store and validate phone numbers.
**Example:** A user can add their phone number to their profile for contact purposes.

**Gender Selection:**
**Purpose:** Allows users to select their gender.
**How it works:** Provides predefined options for gender selection and "other" option for geneder selection if the user wants to selct another selection that not in the list and we handles the errors of invalid gender data to avoid adding invalid selection, user can choose other if he doen't want to sepecifiy it.
**Example:** A user can choose their gender from options like Male, Female, or Other.

**Address Information:**
**Purpose:** Stores users' address details.
**How it works:** Includes fields for address, city, state, country, and ZIP code.
**Example:** A user can update their profile with their full address information.

**Internationalization:**
**Purpose:** Supports multiple languages.
**How it works:** Uses `gettext_lazy` for multi-language support.
**Example:** The app can display user information in different languages based on user preference.

**Custom User Manager (CustomUserManager):**
**create_user(email, password, **extra_fields):** Creates a new user.
**create_superuser(email, password, **extra_fields):** Creates a superuser with necessary permissions.

**Custom User Model (User):**
**Inherits from:** AbstractUser
**Fields:**

- **phone_number:** Stores user's phone number.
- **birth_date:** Stores user's date of birth.
- **gender:** Stores gender (M for male, F for female, O for other).
- **address, city, state, country, zip_code:** Stores address details.
  **Required Fields:** Email, phone number, password, and other personal details.

---

**Meals Overview:**
The Meals App allows users to manage a list of meals, view detailed information about meals, and modify the data. It's essentially a simple system to manage your meals through four main operations: Create, Read, Update, and Delete. These operations are essential for interacting with the meal records in the app.
**CRUD Operations for Meals:**

**Create (C):**
**Purpose:** Allows the user to add new meals to the app.
**How it works:** Users can input information such as meal name, ingredients, and any other details (e.g., calories).
**Example:** A user wants to add a new meal, say, "Grilled Chicken Salad," including all necessary details like ingredients and recipe.

**Read (R):**
**Purpose:** Enables users to view the list of meals or see detailed information about a specific meal.
**How it works:** The app displays a list of all saved meals, or the user can search and click on a specific meal to see its full details.
**Example:** A user wants to look up a meal they saved earlier, like "Vegetable Stir Fry." By clicking on it, they can view its details, including the ingredients and recipe.

**Update (U):**
**Purpose:** Allows the user to modify the details of an existing meal.
**How it works:** The user can select a meal they want to update and make changes to any field, such as the meal's name, ingredients.
**Example:** If a user made some changes to the recipe for "Spaghetti Carbonara" or wants to adjust the calories, they can update the fields.

**Delete (D):**
**Purpose:** Provides the user with the ability to remove a meal from the app.
**How it works:** The user can delete a meal they no longer need or want to keep track of.
**Example:** A user wants to delete a meal that was only added temporarily, like a test meal, or an outdated meal that no longer matches their dietary needs.

---

## The project will be implemented using the following technologies:

    Django
    Django Rest Framework
    PostgreSQL
    Git
    GitHub

## The project will be implemented using the following tools:

    Visual Studio Code
    Postman
    GitHub Desktop

## The project will be implemented using the following programming languages:

    Python
    SQL

## The project will be implemented using the following version control systems:

    Git
    GitHub

## The project will be implemented using the following databases:

    PostgreSQL

## The project will be implemented using the following programming paradigms:

    Object-Oriented Programming (OOP)
    Functional Programming (FP)

## The project will be implemented using the following steps:

1. **Created a new Django project:**

- The `settings.py` and `urls.py` files are added automatically.
- Made initial migrations.
- Updated `settings.py` and `urls.py` to include installed and added apps.

2. **Created a new Django authentication app:**

- The following files were created for the authentication app and the app was implemented using them:
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `serializers.py`
  - `tests.py`
  - `urls.py`
  - `views.py`
- Made Django migrations and checked the status of migrations after every change.
- Tested the app using test cases or Postman.

3. **Created a new Django meals app:**

- The following files were created for the meals app and the app was implemented using them:
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `serializers.py`
  - `tests.py`
  - `urls.py`
  - `views.py`
- Made Django migrations and checked the status of migrations after every change.
- Tested the app using test cases or Postman.

4. **Added main settings and URLs:**

- The main `settings.py` and `urls.py` files are added automatically.

**API Routes**

**API Routes for users' authentication:**
These routes handle user authentication:

| HTTP Method | Endpoint           | Description                                      |
| ----------- | ------------------ | ------------------------------------------------ |
| POST        | /auth/jwt/create/  | Generate an access and refresh token             |
| POST        | /auth/jwt/refresh/ | Refresh the JWT token                            |
| POST        | /auth/jwt/verify/  | Verify if a JWT token is valid                   |
| POST        | /auth/signup/      | Create a new Health Keeper account by signing up |

**API Routes for Meal Management**
These routes manage meals for the Health Keeper:

| HTTP Method | Endpoint                       | Description                             |
| ----------- | ------------------------------ | --------------------------------------- |
| GET         | /meal/meal/{meal_id}/          | Retrieve a meal by its ID               |
| PUT         | /meal/meal/{meal_id}/          | Update a meal by its ID                 |
| DELETE      | /meal/meal/{meal_id}/          | Delete a meal by its ID                 |
| GET         | /meal/meals/                   | List all meals made by Health Keepers   |
| POST        | /meal/meals/                   | Create a new meal for the Health Keeper |
| PUT         | /meal/update-status/{meal_id}/ | Update a meal’s status by its ID        |

**API Routes for User-Specific Meal**
These routes allow filtering meals by user:

| HTTP Method | Endpoint                              | Description                                                     |
| ----------- | ------------------------------------- | --------------------------------------------------------------- |
| GET         | /meal/user/{user_id}/meals/           | Get all meals made by a specific Health Keeper                  |
| GET         | /meal/user/{user_id}/meals/{meal_id}/ | Get details of a specific meal made by a specific Health Keeper |

## The project will be implemented using the following software development practices:

    Test-Driven Development (TDD)
    Behavior-Driven Development (BDD)
    Continuous Integration (CI)
    Continuous Deployment (CD)
    Continuous Delivery (CD)
    Continuous Testing (CT)
    Continuous Monitoring (CM)
    Continuous Feedback (CF)
    Continuous Improvement (CI)
    Continuous Learning (CL)
    Continuous Experimentation (CE)
    Continuous Innovation (CI)
    Continuous Evolution (CE)
    Continuous Adaptation (CA)
    Continuous Change (CC)
    Continuous Transformation (CT)
