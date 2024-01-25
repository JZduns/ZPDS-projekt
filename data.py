import sqlite3
from contextlib import closing

with closing(sqlite3.connect("database/database.db")) as connection:
	with closing(connection.cursor()) as cursor:
	
		cursor.execute("pragma foreign_keys = ON;")
	
		insertTools = """
			insert into tools
			values
				("frying-pan"),
				("colander"),
				("blender"),
				("pot"),
				("microwave"),
				("oven");
		"""
		cursor.execute(insertTools)
		
		insertIngredients = """
			insert into ingredients
			values
				("eggs"),
				("cheese"),
				("pasta"),
				("rice"),
				("ham"),
				("bacon"),
				("flour"),
				("milk");
		"""
		cursor.execute(insertIngredients)
		
		insertUsers = """
			insert into users
			(username, password, email, premium, preferences)
			values 
				("krzysztof323", "september", "krzys323@gmail.com", 1, "without soy");
			"""
		cursor.execute(insertUsers)
		
		insertToolPairs = """
			insert into toolPairs
			(username, toolName)
			values
				("krzysztof323", "frying-pan"),
				("krzysztof323", "blender"),
				("krzysztof323", "oven");
			"""
		cursor.execute(insertToolPairs)
		
		insertIngredientPairs = """
			insert into ingredientPairs
			(username, ingredientName)
			values
				("krzysztof323", "eggs"),
				("krzysztof323", "milk"),
				("krzysztof323", "ham");
			"""
		cursor.execute(insertIngredientPairs)
		
	connection.commit()
				
