# Foodsteps Take-Home Test
There are two tasks to complete: one backend-oriented data processing task and one frontend-oriented task. Here is the link to the Google Drive folder which contains the original README.md and the files for the backend-oriented task [Drive](<https://drive.google.com/drive/folders/1-MsyEuqqXvvyOeg4r8qbhYYZSkrH7c81>).

## Description of Key Files
### Backend Task
- process_impact.py: This script calculates the CO₂ impact of recipes based on the ingredients used. It uses data from the food_classes.csv and recipes.csv files.

- process_impact_streamlit.py: A Streamlit app that provides a user interface for calculating recipe impacts interactively. The app can be found here <https://take-home-test-fs-jdygehunlwkzwbfrcybjhj.streamlit.app/>

- food_classes.csv: Contains food class data, including names, IDs, and CO₂ impacts per kilogram.

- recipes.csv: Contains recipe data, including recipe names and ingredients with weights.

###  Frontend Task
- User_and_Posts_streamlit.py: A Streamlit app that fetches and displays users and their latest posts. The app can be found here <https://take-home-test-fs-dmdb6hg6h2qiqgedej7wfh.streamlit.app/>

- Frontend_App.js: A JavaScript application that fetches user data and their latest posts from a placeholder API and displays them in a user-friendly format. I  am not an expert of JavaScript and React, the Frontend_App.js is essentially based on the code I wrote for the Python version, in simple words, it is a "translation" from Python to Java. 

- src: Folder with the source code of the App.js file.

### Comments
The most difficult part of the challenge for me was the JavaScript. To solve the task, I first used Python because I am more experienced with the language and Streamlit as frontend framework. Then, I did a research online on how to perform the different steps in JavaScript and I used open-source tools to refinish and polish a bit the code. 

The first tasks was very interesting, I personally would use a Jupyter Notebook to solve it. However, the Python script was used as module for the Streamlit app.

The additional streamlit apps were not asked for the task, but for the backend task I had already similar scripts so it was more a personal exercise. For the frontend task it helped me quite a lot in solving the logic behind the problem.

## Supporting Information File
A Jupyter Notebook has been uploaded for a smoother explanation of the different code logics. Here is an exported version to a HTML to visualise it quicker. <file:///Users/sebastiano/Documents/PytonScripts/Foodsteps_CodeChallenge/Notebook_SI.html>