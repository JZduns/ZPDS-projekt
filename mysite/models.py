# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allergies(models.Model):
    username = models.OneToOneField('Users', models.DO_NOTHING, db_column='username', primary_key=True, blank=True, null=True)  # The composite primary key (username, ingredient_name) found, that is not supported. The first column is selected.
    ingredient_name = models.ForeignKey('Ingredients', models.DO_NOTHING, db_column='ingredient_name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allergies'


class Ingredients(models.Model):
    name = models.TextField(primary_key=True, blank=True, null=True)
    is_meat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class IngredientsPairs(models.Model):
    ingredient_name = models.OneToOneField(Ingredients, models.DO_NOTHING, db_column='ingredient_name', primary_key=True, blank=True, null=True)  # The composite primary key (ingredient_name, recipe_name) found, that is not supported. The first column is selected.
    recipe_name = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='recipe_name', blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients_pairs'


class Recipes(models.Model):
    name = models.TextField(primary_key=True, blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipes'


class Users(models.Model):
    username = models.TextField(primary_key=True, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    premium = models.IntegerField(blank=True, null=True)
    vegetarian = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
