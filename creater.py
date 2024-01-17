import sqlite3
import os
import os.path
from contextlib import closing

if not os.path.exists("database"):
	os.mkdir("database")
	
with closing(sqlite3.connect("database/database.db")) as connection:
	with closing(connection.cursor()) as cursor:
	
		cursor.execute("drop table if exists ingredients;")
		createIngredients = """
			create table ingredients
			(
				name text,
				kind text not null,
				primary key (name)
			)
		"""
		cursor.execute(createIngredients)
		
		cursor.execute("drop table if exists recipes;")
		createRecipes = """
			create table recipes
			(
				name text,
				calories integer not null,
				preparation_in_minutes integer not null,
				description_of_preparation text not null,
				thumbs_up integer not null,
				thumbs_down integer not null,
				portions real not null,
				photo blob,
				primary key (name)
			)
		"""
		cursor.execute(createRecipes)
		
		cursor.execute("drop table if exists ingredient_pairs;")
		createIngredientPairs = """
			create table ingredient_pairs
			(
				ingredient_name text,
				recipe_name text,
				level text not null,
				amount float,
				unit text,
				primary key(ingredient_name, recipe_name),
				foreign key (ingredient_name)
				references ingredients(name),
				foreign key (recipe_name)
				references recipes(name)
			)
		"""
		cursor.execute(createIngredientPairs)
		
		cursor.execute("drop table if exists users;")
		createUsers = """
			create table users
			(
				username text,
				password text not null,
				email text,
				premium integer not null,
				preferences text not null,
				primary key (username)
			)
		"""
		cursor.execute(createUsers)
		
		cursor.execute("drop table if exists allergies;")
		createAllergies = """
			create table allergies
			(
				username text,
				allergen_name text,
				primary key (username, allergen_name),
				foreign key (username)
				references users(username),
				foreign key (allergen_name)
				references allergens(name)
			)
		"""
		cursor.execute(createAllergies)
		
		cursor.execute("drop table if exists allergens;")
		createAllergens = """
			create table allergens
			(
				name text,
				primary key(name)
			)
			"""
		cursor.execute(createAllergens)
		
		cursor.execute("drop table if exists allergenPairs;")
		createAllergenPairs = """
			create table allergenPairs
			(
				allergen_name text,
				ingredient_name text,
				primary key(allergen_name, ingredient_name),
				foreign key(allergen_name)
				references allergens(name),
				foreign key(ingredient_name)
				references ingredients(name)
			)
			"""
		cursor.execute(createAllergenPairs)
