import streamlit as st
import requests

# Sidebar navigation
st.title("Users and Posts")

# Fetch data from JSONPlaceholder API
response = requests.get("https://jsonplaceholder.typicode.com/users")
users_data = response.json()

response_posts = requests.get("https://jsonplaceholder.typicode.com/posts")
posts_data = response_posts.json()

# Create a dictionary to hold the latest posts for each user
latest_posts = {}
for post in posts_data:
    user_id = post["userId"]
    post_id = post["id"]
    if user_id not in latest_posts or post_id < latest_posts[user_id]["id"]:
        latest_posts[user_id] = post

# Search bar for filtering
search_term = st.text_input("Search for a user by name:")

# Display users with their latest posts
for user in users_data:
    if search_term.lower() in user["name"].lower():
        st.subheader(user["name"])
        latest_post = latest_posts[user["id"]]
        st.write(f"**Title:** {latest_post['title']}")
        st.write(f"**Body:** {latest_post['body']}")
        st.write("---")