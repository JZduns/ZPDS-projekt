import sqlite3
from contextlib import closing

with closing(sqlite3.connect("database/database.db")) as connection:
	with closing(connection.cursor()) as cursor:
	
	schab = """
		insert into recipes
