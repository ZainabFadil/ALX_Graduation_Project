# Generated by Django 5.1 on 2025-01-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0010_alter_meal_meal_choices_alter_meal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_choices',
            field=models.CharField(blank=True, choices=[('VEGAN', 'vegan'), ('VEGETARIAN', 'vegetarian'), ('PALEO', 'paleo'), ('KETO', 'keto'), ('GLUTEN_FREE', 'gluten free'), ('DAIRY_FREE', 'dairy free'), ('NUT_FREE', 'nut free'), ('SHELLFISH_FREE', 'shellfish free'), ('SOY_FREE', 'soy free'), ('WHEAT_FREE', 'wheat free'), ('EGG_FREE', 'egg free'), ('FISH_FREE', 'fish free'), ('NO_RESTRICTIONS', 'no restrictions')], default='VEGAN', max_length=300),
        ),
        migrations.AlterField(
            model_name='meal',
            name='type',
            field=models.CharField(choices=[('BREAKFAST', 'breakfast'), ('BRUNCH', 'brunch'), ('SNACK', 'snack'), ('LUNCH', 'lunch'), ('DINNER', 'dinner'), ('SUPPER', 'supper')], default='BREAKFAST', max_length=80),
        ),
    ]
