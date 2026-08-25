🌐 Live Demo Streamlit Dashboard: https://aniwise-ai-powered-anime-recommendation-system-lrpc5mtmxkwsiho.streamlit.app/

🎌 AniWise – AI-Powered Anime Recommendation & Analytics System
AniWise is a content-based anime recommendation system developed as a Data Science project. The aim of this project is to help users discover anime that are similar to their favourite titles by analysing anime metadata such as genres, themes, demographics and studios.

Instead of recommending anime based on user watch history, this project focuses on content similarity. Machine learning techniques are used to identify anime with similar characteristics and provide meaningful recommendations.

Along with the recommendation engine, the project also includes exploratory data analysis (EDA), an interactive Power BI dashboard for anime insights, and a Streamlit web application for user interaction.

📌 Project Objectives
The main objectives of this project are:

Perform data cleaning and preprocessing on anime metadata.
Explore the dataset using Exploratory Data Analysis (EDA).
Engineer useful features for machine learning.
Build a content-based recommendation system using KNN.
Develop an interactive Streamlit application.
Create a Power BI dashboard to analyse anime trends and statistics.
🚀 Features
Content-based anime recommendation system
Search anime using title
Supports common English aliases (for example, Attack on Titan → Shingeki no Kyojin)
Displays the most similar anime recommendations
Interactive Streamlit application
Exploratory Data Analysis (EDA)
Power BI dashboard for anime analytics
Clean and modular project structure
🧠 Recommendation Methodology
The recommendation system follows a content-based filtering approach.

The workflow is:

Data Cleaning
Feature Engineering
MultiLabel Encoding
Feature Matrix Creation
K-Nearest Neighbors (KNN)
Cosine Distance Similarity
Top-N Recommendation Generation
The recommendation engine compares anime based on their metadata instead of user ratings or watch history.

📊 Dataset
The project uses the MyAnimeList Recommender Ready Dataset (2025 Edition).

The dataset contains information such as:

Anime Title
Genres
Themes
Demographics
Studios
Score
Type
Episodes
Synopsis
Popularity
Ranking
URL
📈 Exploratory Data Analysis
The following analyses were performed:

Dataset overview
Missing value analysis
Duplicate removal
Distribution of anime types
Top genres
Top studios
Theme analysis
Score distribution
Episode distribution
Popularity analysis
The insights obtained from EDA helped during feature engineering and recommendation model development.

🤖 Machine Learning Approach
Feature Engineering

Genre Encoding
Theme Encoding
Studio Encoding
Demographic Encoding
Machine Learning

MultiLabelBinarizer
K-Nearest Neighbors (KNN)
Cosine Distance
Why KNN?

KNN was selected because it performs well for similarity-based recommendation systems. It compares anime using their encoded metadata and identifies the nearest neighbours based on cosine distance.

💻 Technologies Used
Programming Languages

Python
Libraries

Pandas
NumPy
Scikit-learn
SciPy
Joblib
Matplotlib
Seaborn
Plotly
Streamlit
Tools

Jupyter Notebook
Streamlit
Power BI
Git
GitHub
▶️ How to Run
Clone the repository
git clone https://github.com/Mandeep2807/AniWise-AI-Powered-Anime-Recommendation-System.git
Move into the project folder
cd AniWise-AI-Powered-Anime-Recommendation-System
Install dependencies
pip install -r requirements.txt
Run the Streamlit application
streamlit run app.py
📊 Power BI Dashboard
The project also includes a Power BI dashboard for analysing anime trends.

The dashboard provides insights such as:

Anime type distribution
Top genres
Studio analysis
Score distribution
Popularity analysis
Interactive filtering
🖥️ Streamlit Application
The Streamlit application allows users to:

Search for anime
Receive Top-N recommendations
Explore similar anime
Access anime information through MyAnimeList links
The application provides a simple and interactive interface for exploring recommendations.

📸 Project Screenshots
Home Page
(Add screenshot here)

Recommendation Results
(Add screenshot here)

Power BI Dashboard
(Add screenshot here)

📌 Future Improvements
Possible future enhancements include:

Hybrid recommendation system
User watch history integration
User ratings
Collaborative filtering
Anime poster integration
Advanced search filters
Cloud deployment
👨‍💻 Author
Tamanna

B.Tech Computer Science and Engineering

Lovely Professional University





📜 License
This project is released under the MIT License.
