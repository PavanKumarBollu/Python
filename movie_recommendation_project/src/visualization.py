import matplotlib.pyplot as plt

def plot_rating_distribution(ratings):
    plt.hist(ratings['rating'])
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.show()

def plot_top_genres(movies):
    genres_list = movies['genres'].str.split("|")

    all_genres = []
    for gen in genres_list:
        all_genres.extend(gen)

    genre_counts = {}
    for g in all_genres:
        genre_counts[g] = genre_counts.get(g, 0) + 1

    labels = list(genre_counts.keys())
    sizes = list(genre_counts.values())

    plt.figure(figsize=(12,5))
    plt.bar(labels, sizes)
    plt.xticks(rotation=90)
    plt.title("Top Genres")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.show()
