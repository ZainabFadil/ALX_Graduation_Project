# Generated by Django 5.1 on 2025-01-07 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_rename_ingredients_meal_ingredients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='calories_in_kcals',
            new_name='calories',
        ),
    ]
