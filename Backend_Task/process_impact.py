import pandas as pd
import re
import os

# Load the data from CSV files
# Load the data from CSV files
def load_data():
    current_dir = os.path.dirname(__file__)
    food_classes_df = pd.read_csv(os.path.join(current_dir, 'food_classes.csv'))
    recipes_df = pd.read_csv(os.path.join(current_dir, 'recipes.csv'))
    return food_classes_df, recipes_df

# Function to normalise the name
def normalize_name(name: str) -> str:
    """
    Normalizes a given name by removing punctuation, converting to lowercase,
    and arranging words in alphabetical order.
    
    Input:
    - name (str): The original name string.
    
    Output:
    - str: The normalized name.
    """
    name = re.sub(r'[^\w\s]', '', name)  # Remove any characters that aren't word characters
    name = name.lower()  # Convert to lowercase
    name = ' '.join(sorted(name.split()))  # Arrange words in alphabetical order and join
    return name

# Class to represent a Food Class
class FoodClass:
    """
    Represents a food class in the hierarchy, storing the ID, name, CO₂ impact, 
    and parent class ID.
    
    Attributes:
    - id (int): Unique identifier of the food class.
    - name (str): Name of the food class.
    - impact (float): CO₂ impact per kg of this food class.
    - parent_id (int): ID of the parent class in the hierarchy.
    """
    def __init__(self, id: int, name: str, impact: float, parent_id: int):
        self.id = id
        self.name = name
        self.impact = impact
        self.parent_id = parent_id

# Function to build the food class hierarchy
def build_food_class_hierarchy(df: pd.DataFrame) -> dict:
    """
    Constructs a dictionary to represent the food class hierarchy from a DataFrame.
    
    Input:
    - df (pd.DataFrame): DataFrame containing food class information.
    
    Output:
    - dict: A dictionary mapping each food class ID to a FoodClass instance.
    """
    food_classes = {}
    for _, row in df.iterrows():
        food_classes[row['ID']] = FoodClass(row['ID'], row['Name'], row['Impact / kg'], row['Parent ID'])
    return food_classes

# Recursive function to retrieve impact
def get_impact(food_class_id: int) -> float:
    """
    Recursively calculates the CO2 impact for a given food class ID.
    
    Input:
    - food_class_id (int): The ID of the food class.
    
    Output:
    - float: The CO2 impact per kg for the specified food class.
    
    Raises:
    - ValueError: If the food class or its impact cannot be determined.
    """
    food_class = food_classes.get(food_class_id)
    if not food_class:
        raise ValueError(f"No food class found for ID {food_class_id}")
    if not pd.isna(food_class.impact):
        return food_class.impact
    if pd.isna(food_class.parent_id):
        raise ValueError(f"No impact available and no parent to recurse for {food_class.name}")
    return get_impact(food_class.parent_id)

# Function to calculate the impact for each recipe
def calculate_recipe_impact(recipe: pd.DataFrame) -> float:
    """
    Calculates the total CO₂ impact of a recipe based on its ingredients.

    Input:
    - recipe (pd.DataFrame): DataFrame containing ingredients for a specific recipe.
    
    Output:
    - float: The total CO₂ impact for the recipe.
    
    Returns:
    - None: If any ingredient does not match a food class.
    """
    total_impact = 0
    for _, ingredient in recipe.iterrows():
        ingredient_name = normalize_name(ingredient['Ingredient Name'])
        # Find a matching food class by normalized name
        matched_class = next(
            (fc for fc in food_classes.values() if normalize_name(fc.name) == ingredient_name), None)
        if not matched_class:
            print(f"Ingredient '{ingredient_name}' not found.")
            return None
        try:
            impact = get_impact(matched_class.id)
            total_impact += impact * ingredient['Ingredient Weight / kg']
        except ValueError as e:
            print(e)
            return None
    return total_impact

food_classes_df, recipes_df = load_data()

# Build the food class hierarchy dictionary
food_classes = build_food_class_hierarchy(food_classes_df)

# Process each recipe
for recipe_id, recipe_data in recipes_df.groupby('Recipe ID'):
    recipe_name = recipe_data['Recipe Name'].iloc[0]  # Get the recipe name
    impact = calculate_recipe_impact(recipe_data)
    if impact is not None:
        print(f"Recipe ID {recipe_id} - {recipe_name}: Total Impact = {impact} kg CO2")