import sqlite3
import os
import os.path
from contextlib import closing

if not os.path.exists("database"):
	os.mkdir("database")
	
with closing(sqlite3.connect("database/database.db")) as connection:
	with closing(connection.cursor()) as cursor:
	
		cursor.execute("pragma foreign_keys = ON;")
		
		cursor.execute("drop table if exists toolPairs")
		cursor.execute("drop table if exists ingredientPairs")
		cursor.execute("drop table if exists users")
		cursor.execute("drop table if exists tools")
		cursor.execute("drop table if exists ingredients")
		
		createUsers = """
			create table users
			(
				username text,
				password text not null,
				email text,
				premium integer not null,
				preferences text,
				primary key (username)
			);
		"""
		cursor.execute(createUsers)
		
		createTools = """
			create table tools
			(
				name text,
				primary key (name)
			);
		"""
		cursor.execute(createTools)
		
		createIngredients = """
			create table ingredients
			(
				name text,
				primary key (name)
			);
		"""
		cursor.execute(createIngredients)
		
		createToolPairs = """
			create table toolPairs
			(
				username text,
				toolName text,
				foreign key (username)
				references users(username),
				foreign key (toolName)
				references tools(name),
				primary key (username, toolName)
			);
		"""
		cursor.execute(createToolPairs)
		
		createIngredientPairs = """
			create table ingredientPairs
			(
				username text,
				ingredientName text,
				foreign key (username)
				references users(username)
				foreign key (ingredientName)
				references ingredients(name)
				primary key (username, ingredientName)
			);
		"""
		cursor.execute(createIngredientPairs)
		
	connection.commit()
			
