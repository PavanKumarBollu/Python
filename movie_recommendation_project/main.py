from src.load_data import load_movies, load_ratings
from src.clean_data import clean_movies, clean_ratings
from src.movie_analysis import analyze_movies
from src.recommendation import recommend_popular, recommend_by_genre
from src.visualization import plot_rating_distribution, plot_top_genres

movies = load_movies("data/movies.csv")
ratings = load_ratings("data/ratings.csv")

movies = clean_movies(movies)
ratings = clean_ratings(ratings)

analyze_movies(movies, ratings)

plot_rating_distribution(ratings)
plot_top_genres(movies)

print("\nTop 10 Popular Movies:")
print(recommend_popular(movies, ratings))

print("\nGenre-based recommendations (Action):")
print(recommend_by_genre(movies, "Action"))
