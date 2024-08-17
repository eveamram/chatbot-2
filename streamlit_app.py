from openai import OpenAI
import streamlit as st
from PIL import Image
from recipe_generator import chatbot

# Set up OpenAI API key

##### Setting up the page
## Set the color
with open("Color_Streamlit.py") as f:
    st.markdown(f"<style >{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.title("OpenAI API Key")
openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
client = OpenAI(api_key=openai_api_key)


## Title + Picture
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("<h1 style='color: black;'>Chef</h1>", unsafe_allow_html=True)

with col2:
    image = Image.open('Chef.jpg')
    st.image(image, width=150)

st.markdown("<p style='color: black;'>Hello! I am an AI food chef that generates recipes based on your desires.</p>", unsafe_allow_html=True)

# Create the selectbox with a label
option = st.selectbox("Choose an option:", ["Create a recipe based on ingredients", "Generate a random recipe", "Generate a specific recipe"])

# Choose the type of cuisine
cuisines = ["Any", "American", "Italian", "Chinese", "Mexican", "Indian", "Japanese", "French", "Greek", "Spanish", "Thai"]
selected_cuisine = st.selectbox("Choose a type of cuisine:", cuisines)

if option == "Create a recipe based on ingredients":
    ingredients = st.text_input("Enter your ingredients (comma separated):")
    ingredients_list = [i.strip() for i in ingredients.split(",") if i.strip()]
    st.write("Ingredients you have:", ", ".join(ingredients_list))
    ingredients = ", ".join(ingredients_list)

# Difficulty of dish
difficulty = st.select_slider(
   'Select the difficulty level of the recipe:',
    options=['Easy', 'Medium', 'Hard'],
    value='Medium'  # default value
)

# Food categories in the sidebar
st.sidebar.title("Food Categories")
food_categories = ["Appetizers", "Main Courses", "Desserts"]
selected_category = st.sidebar.selectbox("Select a category:", food_categories)


#Time 
time = st.select_slider(
    'Time you have in minutes',
    options=list(range(5, 120))
)
#Number of people eating
number = st.select_slider(
    'Select the number of people eating: ',
    options=list(range(1, 51)),  # Range from 1 to 50
    value=1  # Default value
)

#Dietary restrictions
restrictions = [
 "Vegetarian",
    "Vegan",
    "Gluten-Free",
    "Dairy-Free",
    "Nut-Free",
    "Soy-Free",
    "Halal",
    "Kosher",
    "Pescatarian",
    "Lactose Intolerance",
    "Egg-Free",
    "Shellfish-Free",
    "Peanut-Free",
    "Diabetic", 
    "Other",
    "None"
]
dietary = st.selectbox("Any dietary restrictions?", restrictions)
if dietary == "Other" :
    dietary = st.text_input("Other:")

# Button to generate recipes
if st.button("Generate Recipe"):
    with st.spinner("Generating recipe..."):
    
     prompt = f"""You may add other ingredients, but the recipe must feature these specified ingredients: {ingredients}.
        The recipe should be at a {difficulty} difficulty level and reflect the flavors and techniques of {selected_cuisine} cuisine.
        The recipe should take no more than {time} minutes to prepare, be suitable for {number} people, and adhere to the following dietary restriction: {dietary}.
        """
     st.write(chatbot(prompt, client))
