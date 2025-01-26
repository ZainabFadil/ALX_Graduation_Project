# Generated by Django 5.1 on 2025-01-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_rename_calories_meal_calories_in_kcals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='Ingredients',
            field=models.TextField(default='Ingredients'),
        ),
        migrations.AddField(
            model_name='meal',
            name='Recipe',
            field=models.TextField(default='Recipe'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='description',
            field=models.TextField(default='Description'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='minerals',
            field=models.TextField(default='Minerals'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='vitamins',
            field=models.TextField(default='Vitamins'),
        ),
    ]
