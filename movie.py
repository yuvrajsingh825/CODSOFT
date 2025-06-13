import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV file
try:
    df = pd.read_csv("movies.csv")
except FileNotFoundError:
    print("❌ movies.csv not found.")
    exit()

# Check required columns
if 'title' not in df.columns or 'genre' not in df.columns:
    print("❌ CSV must have 'title' and 'genre' columns.")
    exit()

# Clean data
df['title'] = df['title'].astype(str).str.strip()
df['genre'] = df['genre'].fillna('')

# Convert genre strings into a list of tags
cv = CountVectorizer(tokenizer=lambda x: x.split('|'), token_pattern=None)
genre_matrix = cv.fit_transform(df['genre'])

# Calculate cosine similarity between all movies
similarity = cosine_similarity(genre_matrix)

# Recommend movies
def recommend(movie_name):
    # Make title matching case-insensitive and strip spaces
    titles = df['title'].str.lower().str.strip()
    movie_name_lower = movie_name.lower().strip()
    if movie_name_lower not in titles.values:
        print("❌ Movie not found in dataset.")
        return

    # Get the index of the movie
    index = titles[titles == movie_name_lower].index[0]
    # Get similarity scores for that movie
    similarity_scores = list(enumerate(similarity[index]))
    # Sort the movies based on similarity scores
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]  # top 5 recommendations

    # Print recommendations
    print(f"\n🎬 Top Recommendations for '{df.iloc[index]['title']}':")
    for i in sorted_scores:
        print("•", df.iloc[i[0]]['title'])

# Run the recommender
if __name__ == "__main__":
    movie = input("Enter a movie you like: ")
    recommend(movie)