# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Allergies(models.Model):
    username = models.OneToOneField('Profiles', models.DO_NOTHING, db_column='username', primary_key=True, blank=True)  # The composite primary key (username, ingredient_name) found, that is not supported. The first column is selected.
    ingredient_name = models.ForeignKey('Ingredients', models.DO_NOTHING, db_column='ingredient_name', blank=True, null=True)

    class Meta:
        db_table = 'allergies'


class Ingredients(models.Model):
    name = models.TextField(primary_key=True, blank=True)
    is_meat = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ingredients'


class IngredientsPairs(models.Model):
    ingredient_name = models.OneToOneField(Ingredients, models.DO_NOTHING, db_column='ingredient_name', primary_key=True, blank=True)  # The composite primary key (ingredient_name, recipe_name) found, that is not supported. The first column is selected.
    recipe_name = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='recipe_name', blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ingredients_pairs'


class Recipes(models.Model):
    name = models.TextField(primary_key=True, blank=True)
    calories = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True,null=True)

    class Meta:
        db_table = 'recipes'


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    premium = models.BooleanField(blank=True, null=True)
    vegetarian = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'profiles'
