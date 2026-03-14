import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

movies_path = BASE_DIR / "data" / "movies.csv"
credits_path = BASE_DIR / "data" / "credits.csv"

def load_data():

    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    movies = movies.merge(credits, on="title")

    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

    movies.dropna(inplace=True)

    movies['tags'] = movies['overview'] + movies['genres']

    return movies