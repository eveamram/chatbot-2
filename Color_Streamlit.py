/* styles.css */ 

body, h2, h3, h4, h5, h6, p, div, span, label, .stText, .stSelectbox {
    color: black;
    background-color: #f0f0f0; 
    font-size: 16px; /* Smaller font size for general text */
}

h1 {
    font-size: 50px; 
    font-weight: bold; 
}

.stSelectbox > div > div > div > div {
    color: bluegray;
}

/* Add outline to the select box */ 
.stSelectbox > div > div {
    outline: 2px solid lightcoral; /* Reverted outline color */
    border-radius: 3px; /* Optional: add border radius */
    font-size: 16px; /* Match the smaller general text size */
}

.stButton > button {
    color: black;
    border: 2px solid lightcoral; /* Reverted border color */
    background-color: transparent;
    border-radius: 3px;
    font-size: 16px; /* Match the smaller general text size */
}

.stTextInput > div > div > input {
    color: black;
    border: 2px solid lightcoral; /* Reverted border color */
    background-color: transparent;
    border-radius: 3px;
    font-size: 16px; /* Match the smaller general text size */
}