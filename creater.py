import sqlite3
import os
import os.path
from contextlib import closing

if not os.path.exists("database"):
	os.mkdir("database")
	
with closing(sqlite3.connect("database/database.db")) as connection:
	with closing(connection.cursor()) as cursor:
		createIngredients = """
			create table if not exists ingredients
			(
				name text,
				is_meat integer,
				primary key (name)
			)
		"""
		cursor.execute(createIngredients)
		
		createRecipes = """
			create table if not exists recipes
			(
				name text,
				calories integer,
				primary key (name)
			)
		"""
		cursor.execute(createRecipes)
		
		createIngredientPairs = """
			create table if not exists ingredients_pairs
			(
				ingredient_name text,
				recipe_name text,
				level integer,
				foreign key (ingredient_name)
				references ingredients(name),
				foreign key (recipe_name)
				references recipes(name)
			)
		"""
		cursor.execute(createIngredientPairs)
		
		createUsers = """
			create table if not exists users
			(
				username text,
				password text,
				email text,
				premium integer,
				vegetarian integer,
				primary key (username)
			)
		"""
		cursor.execute(createUsers)
