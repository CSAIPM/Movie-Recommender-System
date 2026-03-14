import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

movies_path = BASE_DIR / "data" / "movies.csv"

df = pd.read_csv(movies_path)

print(df.head())

# Top genres distribution
df['genres'].value_counts().head(10)

# Popularity distribution
sns.histplot(df["popularity"], kde=True)

plt.title("Movie Popularity Distribution")

plt.show()