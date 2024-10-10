import streamlit as st
import pandas as pd
import os
from process_impact import *  # Import your custom module

current_dir = os.path.dirname(__file__)
food_classes_df = pd.read_csv(os.path.join(current_dir, 'food_classes.csv'))
recipes_df = pd.read_csv(os.path.join(current_dir, 'recipes.csv'))

# Sidebar navigation
st.title("Recipe Impact Calculator")
st.write("This app allows the user to preview the recipes data and to calculate recipe impacts by clicking the button below.")

# Show raw data for recipes
st.header("Recipes Data")
st.write("Below is a preview of the recipes data:")
st.write(recipes_df.head())  # Show the head of recipes data

# Button to calculate impacts
if st.button("Calculate Recipe Impacts"):
    st.header("Recipe Impact Results")
    
    # Process each recipe and calculate impact
    try:
        impacts = {}
        for recipe_id, recipe_data in recipes_df.groupby('Recipe ID'):
            recipe_name = recipe_data['Recipe Name'].iloc[0]
            impact = calculate_recipe_impact(recipe_data)  # Make sure this function is defined
            if impact is not None:
                impacts[recipe_id] = (recipe_name, impact)
        
        for recipe_id, (recipe_name, impact) in impacts.items():
            st.write(f"Recipe ID {recipe_id} - {recipe_name}: Total Impact = {impact:.2f} kg CO2")
    except Exception as e:
        st.error(f"Error: {e}")