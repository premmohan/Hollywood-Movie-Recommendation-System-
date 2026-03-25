import streamlit as st
import pickle
import joblib
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

# -------------------------------
# Custom CSS (Final Styling)
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* ✅ Hollywood Background Wallpaper */
.stApp {
    background-image: 
        linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
        url("https://images.unsplash.com/photo-1542204165-65bf26472b9b");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

/* Selectbox Label */
.stSelectbox label {
    font-size: 43px !important;
    font-weight: 600 !important;
    color: #ffffff !important;
}

/* Dropdown text */
div[data-baseweb="select"] > div {
    font-size: 20px !important;
    font-weight: 500 !important;
}

/* Button */
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3.2em;
    width: 100%;
    font-size: 21px;
    font-weight: 600;
    margin-top: 10px;
    border: none;
}

.stButton>button:hover {
    background-color: #ff4b4b !important;
    color: white !important;
}

.stButton>button:focus {
    outline: none !important;
    box-shadow: none !important;
}

/* Recommendation title */
.reco-title {
    font-size: 28px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 15px;
    color: #bbbbbb
}

/* Movie cards */
.movie-card {
    background-color: #1c1f26;
    color: white !important;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    border-left: 5px solid #ff4b4b;
    font-size: 22px;
    font-weight: 500;
    letter-spacing: 0.5px;
}

/* Fix transparent header bar */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0) !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------

st.markdown("<h1 style='text-align:center; color:#ff4b4b; font-size:44px; font-weight:700;'>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align:center; color:#bbbbbb; font-weight:500;'>AI-powered movie recommendations in one click</h4>",
    unsafe_allow_html=True)

# -------------------------------
# Load Data
# -------------------------------
with open("movies.pickle", "rb") as m:
    movies = pickle.load(m)

similarity = joblib.load("similarity.joblib")
movies_names = movies["title"].values

# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    similarity_scores = similarity[movie_index]

    movies_list = sorted(
        enumerate(similarity_scores),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movies_list]

# -------------------------------
# UI Input
# -------------------------------
#st.subheader("🎥 Choose a Movie")
st.markdown("<h3 style='color:#bbbbbb; font-size:27px;'>🎥 Choose a Movie</h3>", unsafe_allow_html=True)
selected_movie = st.selectbox("", movies_names)

# -------------------------------
# Recommendation Button
# -------------------------------
if st.button(" ✨ RECOMMEND MOVIES", use_container_width=True):
    recommendations = recommend(selected_movie)

    st.markdown("<h3 style='color:#bbbbbb; font-size:27px; font-weight:700;'>🍿 Recommended Movies</h3>", unsafe_allow_html=True)
    for movie in recommendations:
        st.markdown(f'<div class="movie-card">{movie}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style="color:#bbbbbb; text-align: center;">Built by PREM MOHAN</p>",
    unsafe_allow_html=True
)
