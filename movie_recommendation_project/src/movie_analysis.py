def analyze_movies(movies, ratings):
    print("Movies:", len(movies))
    print("Ratings:", len(ratings))

    avg_ratings = ratings.groupby("movieId")["rating"].mean()
    highest_rated = avg_ratings.sort_values(ascending=False).head(10)

    print("\nTop 10 Highest Rated Movies:")
    print(highest_rated)
