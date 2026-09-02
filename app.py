
import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os


MOVIE_URL = "https://github.com/B-Samy/Movie-Recomendation-System/releases/download/v1.0.0/movie_dict.pkl"

SIMILARITY_URL = "https://github.com/B-Samy/Movie-Recomendation-System/releases/download/v1.0.0/simalirity.pkl"




def download_file(url, filename):

    if not os.path.exists(filename):

        response = requests.get(
            url,
            stream=True,
            timeout=300
        )

        response.raise_for_status()

        with open(filename, "wb") as file:

            for chunk in response.iter_content(
                chunk_size=1024 * 1024
            ):

                if chunk:
                    file.write(chunk)


download_file(
    MOVIE_URL,
    "movie_dict.pkl"
)

download_file(
    SIMILARITY_URL,
    "simalirity.pkl"
)


movie_dict = pickle.load(
    open("movie_dict.pkl", "rb")
)

similarity = pickle.load(
    open("simalirity.pkl", "rb")
)

movies = pd.DataFrame(movie_dict)

st.set_page_config(
    page_title="MovieGPT",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.caption("Made by Shaheer Rangrej")

TMDB_API_KEY = st.secrets["TMDB_API_KEY"]

session = requests.Session()

retry = Retry(
    total=5,
    connect=5,
    read=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("https://", adapter)
session.mount("http://", adapter)


def fetch_poster(movie_id):

    try:

        response = session.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}",
            params={
                "api_key": TMDB_API_KEY
            },
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return "https://placehold.co/500x750?text=No+Poster"

    except requests.exceptions.RequestException:

        return "https://placehold.co/500x750?text=No+Poster"


def recommend(movie):

    movie_index = movies[
        movies["title"] == movie
    ].index[0]

    distance = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters






# movie_dict = pickle.load(
#     open("movie_dict.pkl", "rb")
# )

# similarity = pickle.load(
#     open("simalirity.pkl", "rb")
# )

# movies = pd.DataFrame(movie_dict)







st.title("🎬 MovieGPT")

st.subheader(
    "Discover movies you'll love using AI-powered recommendations."
)

st.divider()

select_movie_name = st.selectbox(
    "Choose a movie you like",
    movies["title"].values
)

recommend_button = st.button(
    "✨ Find My Recommendations",
    type="primary",
    use_container_width=True
)

st.markdown("""
<style>
.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #DB2777);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #6D28D9, #BE185D);
    color: white;
}
</style>
""", unsafe_allow_html=True)

if recommend_button:

    with st.spinner("Finding movies you might love..."):

        names, posters = recommend(
            select_movie_name
        )

    st.divider()

    st.header(
        f"Because you liked {select_movie_name}"
    )

    st.write(
        "Here are 5 movies selected based on similarity."
    )

    cols = st.columns(5)

    for i in range(5):

        with cols[i]:

            st.caption(
                f"Recommendation {i + 1}"
            )

            st.image(
                posters[i],
                use_container_width=True
            )

            st.subheader(
                names[i]
            )

    st.divider()

    st.metric(
        label="Personalized recommendations generated",
        value="5"
    )

st.divider()

st.caption(
    "🎬 Shaheer Rangrej · Movie Recommendation System"
)

