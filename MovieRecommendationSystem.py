import pandas as pd
import numpy as np
import sys

data = {
        'Title': [
            'Inception', 'The Dark Knight', 'Titanic', 'Avatar',
            'The Matrix'
        ],
        'Genre': [
            'Sci-Fi', 'Action', 'Romance', 'Sci-Fi',
            'Sci-Fi'
        ],
        'Rating': [
            4.8, 4.9, 4.7, 4.6,
            4.5
        ],
        'ReleaseYear': [
            2010, 2008, 1997, 2009,
            1999
        ],
        'Popularity': [
            12000, 15000, 13000, 14000,
            9000
        ]
    }

def display_Data():
    movies_df = pd.DataFrame(data)
    print(movies_df)



print("Welcome to Movie reccomendation System")
print("Here are the movies for you:")
display_Data()

