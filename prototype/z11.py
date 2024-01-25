import streamlit as st
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the HTML template for the front end with custom styles
html_temp = """
    <style>
    body {
        background-color: #F6F6F6;  /* Set the background color to gold */
        font-family: Arial, sans-serif;  /* Set the font family */
    }
    h1 {
        color: #1E56A0;  /* Set the h1 (title) color to dark gray */
    }
    </style>
    <div style="background-color:#F6F6F6;padding:13px;text-align:center;">
    <h1 style="color: #FF0000;">ugotowAI</h1>
    </div>
"""

# Set the page configuration
st.set_page_config(
    page_title="ugotowAI",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon=None,
)

# Display the front end aspect
st.markdown(html_temp, unsafe_allow_html=True)

# Add a picture of food
# Center-align the image using st.image
st.image("./pexel.jpg", use_column_width=True)

user_input = st.text_input("Wpisz składniki: ")

df = pd.read_csv('./Food Ingredients and Recipe Dataset with Image Name Mapping.csv')
df = df[['Title', 'Cleaned_Ingredients']]

def dod_do_list(user_input, list_sklad):
    if user_input:
        list_sklad.append(user_input.strip())
        st.session_state.lista_skladnikow = list_sklad  # Aktualizuj listę w kontekście sesji

if 'lista_skladnikow' not in st.session_state:
    st.session_state.lista_skladnikow = []
if st.button("Dodaj składnik"):
    dod_do_list(user_input,st.session_state.lista_skladnikow)
    #st.write(st.session_state.lista_skladnikow)
    print(st.session_state.lista_skladnikow)

if 'lista_skladnikow' in st.session_state and st.session_state.lista_skladnikow:
    st.write("Lista składników:", st.session_state.lista_skladnikow)

def dod_do_list_al(user_input, list_sklad_al):
    if user_input:
        list_sklad_al.append(user_input.strip())
        st.session_state.lista_alergenow = list_sklad_al  # Aktualizuj listę w kontekście sesji

if 'lista_alergenow' not in st.session_state:
    st.session_state.lista_alergenow = []
alerg_input = st.text_input("Wpisz alergen: ")
if st.button("Dodaj alergen"):
    dod_do_list_al(alerg_input, st.session_state.lista_alergenow)
   # st.write("Aktualna lista alergenów:", st.session_state.lista_alergenow)
    print(st.session_state.lista_alergenow)

if 'lista_alergenow' in st.session_state and st.session_state.lista_alergenow:
    st.write("Lista alergenów:", st.session_state.lista_alergenow)

def dod_do_list_sp(user_input, list_sklad_sp):
    if user_input:
        list_sklad_sp.append(user_input.strip())
        st.session_state.lista_sprzetow = list_sklad_sp  # Aktualizuj listę w kontekście sesji

if 'lista_sprzetow' not in st.session_state:
    st.session_state.lista_sprzetow = []
sprz_input = st.text_input("Wprowadź sprzęt kuchenny: ")
if st.button("Dodaj sprzęt kuchenny"):
    dod_do_list_sp(sprz_input, st.session_state.lista_sprzetow)
    #st.write("Aktualna lista sprzętów:", st.session_state.lista_sprzetow)
    print(st.session_state.lista_sprzetow)

if 'lista_sprzetow' in st.session_state and st.session_state.lista_sprzetow:
    st.write("Lista sprzętów:", st.session_state.lista_sprzetow)

def dod_do_list_cz(user_input, list_sklad_cz):
    if user_input:
        list_sklad_cz.append(user_input.strip())
        st.session_state.lista_czasow = list_sklad_cz  # Aktualizuj listę w kontekście sesji

if 'lista_czasow' not in st.session_state:
    st.session_state.lista_czasow = []
tim_input = st.text_input("Podaj maksymalny czas przygotowania: ")
if st.button("Dodaj czas"):
    dod_do_list_cz(tim_input, st.session_state.lista_czasow)
   # st.write("Czas:", st.session_state.lista_czasow)
    print(st.session_state.lista_czasow)

if 'lista_czasow' in st.session_state and st.session_state.lista_czasow:
    st.write("Lista czasów:", st.session_state.lista_czasow)

st.write("Lista która wleci do algorytmu: ")

combined_list = []

if 'lista_skladnikow' in st.session_state:
    combined_list.extend(st.session_state.lista_skladnikow)
if 'lista_alergenow' in st.session_state:
    combined_list.extend(st.session_state.lista_alergenow)
if 'lista_sprzetow' in st.session_state:
    combined_list.extend(st.session_state.lista_sprzetow)
if 'lista_czasow' in st.session_state:
    combined_list.extend(st.session_state.lista_czasow)
combined_string=''
if combined_list:
    combined_string = ",".join(combined_list)
    st.write("Połączona lista wszystkich elementów:", combined_string)

#nie ruszac tego nizej#
def recommend_dishes(data, user_input):
    # Preprocess user input
    user_input = user_input.lower()

    # Calculate the number of matching ingredients
    vectorizer = CountVectorizer()
    ingredients_matrix = vectorizer.fit_transform(data['Cleaned_Ingredients'])

    user_vector = vectorizer.transform([user_input])

    similarities = cosine_similarity(user_vector, ingredients_matrix)

    # Find dishes with at least `threshold` matching ingredients
    matching_dishes = [(index, row) for index, row in enumerate(similarities[0]) if row >= 0.3]

    recommended_dishes = data.iloc[[index for index, _ in matching_dishes]]

    return recommended_dishes[['Title', 'Cleaned_Ingredients']]
# if st.button("Wyszukaj przepisy"):
#     if user_input:
#         recommended_dishes = recommend_dishes(df, user_input)
#         st.subheader("Recommended Dishes:")
#
#         if not recommended_dishes.empty:
#             # Create a dictionary to store whether the ingredients expander is open for each dish
#             expanders_open = {}
#
#             for idx, row in recommended_dishes.iterrows():
#                 title = row['Title']
#                 cleaned_ingredients = row['Cleaned_Ingredients']
#
#                 # Create an expander for each dish
#                 with st.expander(f"{title}", expanded=expanders_open.get(title, False)):
#
#                     # st.markdown(cleaned_ingredients)
#                     # Split the ingredients string at the comma
#                     ingredients_list = [ingredient.lstrip("'") for ingredient in cleaned_ingredients.split("', ")]
#
#                     # Remove "for serving" from each ingredient
#                     ingredients_list = [ingredient.replace('for serving', '') for ingredient in ingredients_list]
#
#                     # Check if the first ingredient starts with "[" and remove it
#                     if ingredients_list[0].startswith("['"):
#                         ingredients_list[0] = ingredients_list[0][2:]
#
#                     # Check if the last ingredient ends with ']'
#                     if ingredients_list[-1].endswith("']"):
#                         ingredients_list[-1] = ingredients_list[-1][:-2]
#
#                     st.markdown('\n'.join([f"- {ingredient}" for ingredient in ingredients_list]))
#         else:
#             st.write("No recommended dishes found. Please try a different combination of ingredients.")
#
#
#     else:
#         st.warning("Please enter ingredients to get recommendations.")
#



print(combined_string)

if st.button("Wyszukaj przepisy"):
    if combined_string:
        recommended_dishes = recommend_dishes(df, combined_string)
        st.subheader("Recommended Dishes:")

        if not recommended_dishes.empty:
            # Create a dictionary to store whether the ingredients expander is open for each dish
            expanders_open = {}

            for idx, row in recommended_dishes.iterrows():
                title = row['Title']
                cleaned_ingredients = row['Cleaned_Ingredients']

                # Create an expander for each dish
                with st.expander(f"{title}", expanded=expanders_open.get(title, False)):

                    # st.markdown(cleaned_ingredients)
                    # Split the ingredients string at the comma
                    ingredients_list = [ingredient.lstrip("'") for ingredient in cleaned_ingredients.split("', ")]

                    # Remove "for serving" from each ingredient
                    ingredients_list = [ingredient.replace('for serving', '') for ingredient in ingredients_list]

                    # Check if the first ingredient starts with "[" and remove it
                    if ingredients_list[0].startswith("['"):
                        ingredients_list[0] = ingredients_list[0][2:]

                    # Check if the last ingredient ends with ']'
                    if ingredients_list[-1].endswith("']"):
                        ingredients_list[-1] = ingredients_list[-1][:-2]

                    st.markdown('\n'.join([f"- {ingredient}" for ingredient in ingredients_list]))
        else:
            st.write("No recommended dishes found. Please try a different combination of ingredients.")


    else:
        st.warning("Please enter ingredients to get recommendations.")

