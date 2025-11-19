def recommend_popular(movies, ratings, top_n=10):
    popularity = ratings.groupby("movieId")["rating"].count()
    popularity = popularity.sort_values(ascending=False).head(top_n)

    popular_movies = movies[movies['movieId'].isin(popularity.index)]
    return popular_movies[['movieId', 'title', 'genres']]

def recommend_by_genre(movies, genre):
    genre = genre.lower()
    filtered = movies[movies['genres'].str.lower().str.contains(genre)]
    return filtered[['movieId', 'title', 'genres']].head(10)
