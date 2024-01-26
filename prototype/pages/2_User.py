import sqlite3
import streamlit as st

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()
# users: username, password, email, premium, preferences
query = "SELECT username, email, premium, preferences FROM users"
cursor.execute(query)
user = cursor.fetchone()
conn.close()

st.write("Nazwa użytkownika: "+user[0])
st.write("Adres e-mail: "+user[1])
if user[2] == 1:
    st.write("Konto Premium")
st.write("Preferencje żywnościowe: "+user[3])
