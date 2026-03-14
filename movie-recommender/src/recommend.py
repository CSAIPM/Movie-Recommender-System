import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

similarity = joblib.load(BASE_DIR / "models" / "similarity.pkl")
movies = joblib.load(BASE_DIR / "models" / "movies.pkl")

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movie_list:
        print(movies.iloc[i[0]].title)

recommend("Avatar")