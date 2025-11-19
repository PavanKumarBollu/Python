import pandas as pd

def load_movies(path):
    return pd.read_csv(path)

def load_ratings(path):
    return pd.read_csv(path)
