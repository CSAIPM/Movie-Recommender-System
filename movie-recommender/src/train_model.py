import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from pathlib import Path

from preprocess import load_data

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "similarity.pkl"
MOVIE_DATA = BASE_DIR / "models" / "movies.pkl"

movies = load_data()

cv = CountVectorizer(max_features=5000, stop_words="english")

vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

joblib.dump(similarity, MODEL_PATH)
joblib.dump(movies, MOVIE_DATA)

print("Recommender model saved.")