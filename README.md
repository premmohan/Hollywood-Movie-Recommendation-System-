# Hollywood-Movie-Recommendation-System-
AI-powered Hollywood movie recommender system built with Python, NLP, and Streamlit

Overview
This project uses Natural Language Processing (NLP) to recommend movies. By analyzing "tags" (a combination of genres, keywords, cast, and crew), the system calculates the mathematical similarity between films to find the best matches for any given title.

Key Features
Smart Search: Select from a database of 4,800+ Hollywood movies.
Instant Recommendations: Displays the Top 5 most similar movies side-by-side.
Sleek UI: Dark-themed, responsive interface designed with Streamlit and Custom CSS.

🛠️ Tech Stack
Language: Python 3.12
Data Analysis: Pandas, NumPy
Machine Learning: Scikit-Learn (CountVectorizer, Cosine Similarity)
Web Framework: Streamlit
Version Control: Git & GitHub

How It Works
Data Preprocessing: Cleaned the TMDB 5000 Movies dataset, extracting essential information from JSON-formatted columns (genres, keywords, cast, and crew).
Feature Engineering: Combined metadata into a single "tags" column for every movie.
Vectorization: Converted text tags into 5,000-dimensional vectors using CountVectorizer (Bag of Words).
Cosine Similarity: Calculated the "distance" between movie vectors. The closer two vectors are in space, the more similar the movies are.
