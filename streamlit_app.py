import streamlit as st
import openai  # Assuming you're using OpenAI's API for recipe generation
from PIL import Image
import os

# Set up OpenAI API key
openai.api_key = ''

##### Setting up the page
## Set the color
with open("Color_Streamlit.py") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

##Title+Picture
col1, col2 = st.columns([1,3])
with col1:
   st.markdown("<h1 style='color: black;'>Chef</h1>", unsafe_allow_html=True)

with col2:
    image = Image.open('Chef.jpg')
    st.image(image,width=150)
  
st.markdown("<p style='color: black;'>Hello! I am an AI food chef that generates recipes based on your desires.</p>", unsafe_allow_html=True)



# Create the selectbox with a label

option = st.selectbox("Choose an option:", ["Create a recipe based on ingredients", "Generate a random recipe", "Generate a specific recipe"])

#Choose the type of cuisine
cuisines = ["Any", "Italian", "Chinese", "Mexican", "Indian", "Japanese", "French", "Greek", "Spanish", "Thai"]
selected_cuisine = st.selectbox("Choose a type of cuisine:", cuisines)

if option == "Create a recipe based on ingredients":
    ingredients = st.text_input("Enter your ingredients (comma separated):") #sidebar.selectbox
    ingredients_list = [i.strip() for i in ingredients.split(",") if i.strip()]
    st.write("Ingredients you have:", ", ".join(ingredients_list))

#Difficulty of dish
difficulty = st.select_slider(
    'Select the difficulty level of the recipe:',
    options=['Easy', 'Medium', 'Hard'],
    value='Medium'  # default value
    
)
##Button to generate recipes
if st.button("Generate Recipe"):
    # Placeholder action for when the button is clicked
    st.write("Generating recipe...")


st.sidebar.title("Food Categories")
food_categories = ["Appetizers", "Main Courses", "Desserts",]
selected_category = st.sidebar.selectbox("Select a category:", food_categories)



