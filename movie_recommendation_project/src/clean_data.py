def clean_movies(df):
    df['genres'] = df['genres'].astype(str)
    return df

def clean_ratings(df):
    df = df[df['rating'] > 0]
    return df
