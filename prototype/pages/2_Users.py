import sqlite3
import streamlit as st

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

# users: username, password, email, premium, preferences
query = "SELECT username, email, premium, preferences FROM users"

cursor.execute(query)
results = cursor.fetchall()

conn.close()

st.write("Użytkownicy:")
st.write(results)
