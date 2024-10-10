import streamlit as st
import pandas as pd
from process_impact import *  # Import your custom module

# Load data
recipes_df = pd.read_csv('recipes.csv')

# Sidebar navigation
st.sidebar.title("Recipe Impact Calculator")
st.sidebar.write("Select an option to view data or calculate recipe impacts.")

# Show raw data for recipes
st.header("Recipes Data")
st.write("Below is a preview of the recipes data:")
st.write(recipes_df.head())  # Show the head of recipes data

# Button to calculate impacts
if st.button("Calculate Recipe Impacts"):
    st.header("Recipe Impact Results")

    # Process each recipe and calculate impact
    try:
        # Assuming process_all_recipes returns a dictionary with impacts
        impacts = process_all_recipes(recipes_df)
        st.write("Calculated Impacts for Recipes:")
        
        # Display results with recipe name, ID, and impact
        for recipe_id, impact in impacts.items():
            # Extract recipe name for each recipe ID
            recipe_name = recipes_df[recipes_df['Recipe ID'] == recipe_id]['Recipe Name'].iloc[0]
            if impact is not None:
                st.write(f"Recipe ID {recipe_id} - {recipe_name}: Total Impact = {impact:.2f} kg CO2")
            else:
                st.write(f"Ingredient not found in Recipe ID {recipe_id} - {recipe_name}")
    except Exception as e:
        st.error(f"Error: {e}")