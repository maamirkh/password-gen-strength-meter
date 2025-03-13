import streamlit as st  # Import the Streamlit library
import random  # Import the random library
import string  # Import the string library

def generate_password(length, use_digits, use_special):  
    characters = string.ascii_letters  # Include all lowercase and uppercase letters

    if use_digits:  
        characters += string.digits  # Add digits 0-9  

    if use_special:  
        characters += string.punctuation  # Add special characters  

    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    length_score = len(password) >= 12  # 12 se bara length achi hoti hai
    digit_score = any(char.isdigit() for char in password)  # Koi bhi number hai?
    special_score = any(char in string.punctuation for char in password)  # Koi bhi special character hai?

    score = sum([length_score, digit_score, special_score])

    if score == 3:
        return "🟢 Strong"
    elif score == 2:
        return "🟡 Medium"
    else:
        return "🔴 Weak"

st.title("🔐 Password Generator")  

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)  
use_digits = st.checkbox("Include Digits")  
use_special = st.checkbox("Include Special Characters")  

if st.button("Generate Password"):  
    password = generate_password(length, use_digits, use_special)  
    strength = check_password_strength(password)  
    st.write(f"**Generated Password:** `{password}`")  
    st.write(f"**Password Strength:** {strength}")  

st.write("----------------")  
