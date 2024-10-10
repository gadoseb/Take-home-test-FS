import React, { useEffect, useState } from 'react';

function App() {
  // State variables to store user data, post data, filtered users, and the search term
  const [users, setUsers] = useState([]);
  const [posts, setPosts] = useState([]);
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');

  // Load the data when the component mounts
  useEffect(() => {
    // Define a function to fetch data from APIs
    const fetchData = async () => {
      try {
        // Fetch users
        const usersResponse = await fetch('https://jsonplaceholder.typicode.com/users');
        const usersData = await usersResponse.json();

        // Fetch posts
        const postsResponse = await fetch('https://jsonplaceholder.typicode.com/posts');
        const postsData = await postsResponse.json();

        // Save data to state
        setUsers(usersData);
        setPosts(postsData);
        setFilteredUsers(usersData); // Initially display all users
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData(); // Call the function we just defined
  }, []); // Empty array as second argument means this only runs once

  // Update the filtered users whenever the search term changes
  useEffect(() => {
    const filtered = users.filter(user =>
      user.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredUsers(filtered);
  }, [searchTerm, users]);

  // Function to get the latest post for a user
  const getLatestPost = (userId) => {
    // Find posts for this user
    const userPosts = posts.filter(post => post.userId === userId);
    if (userPosts.length === 0) return null;

    // Sort the posts by ID, so the last one is the most recent
    userPosts.sort((a, b) => b.id - a.id);
    return userPosts[0]; // Return the latest post
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>User Posts</h1>

      {/* Search Bar */}
      <input
        type="text"
        placeholder="Search users by name"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)} // Update searchTerm whenever input changes
        style={{ padding: '10px', width: '100%', marginBottom: '20px' }}
      />

      {/* User List */}
      <div>
        {filteredUsers.map(user => {
          const latestPost = getLatestPost(user.id); // Get the latest post for each user

          return (
            <div key={user.id} style={{ borderBottom: '1px solid #ccc', marginBottom: '20px', paddingBottom: '20px' }}>
              <h2>{user.name}</h2>
              {latestPost ? (
                <div>
                  <h3>{latestPost.title}</h3>
                  <p>{latestPost.body}</p>
                </div>
              ) : (
                <p>No posts available.</p>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default App;