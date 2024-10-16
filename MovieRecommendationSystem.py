import pandas as pd
import numpy as np
import sys
import random

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
movies_df = pd.DataFrame(data)
    
def display_Data():
    print(movies_df)

def filter_data_on_genre(genre):
    print(movies_df[movies_df['Genre'] == genre])

def filter_data_on_ratings(min_rating):
    print("Here is the filtered data")
    print(movies_df[movies_df['Rating']>=min_rating])

def get_avg_ratings_of_films():
    print(movies_df['Rating'].mean())

def get_random_movie_selection():
    length = len(movies_df)
    random_num = random.randint(0,length-1)
    movie = np.array(movies_df['Title'])
    print(f"Random movie recommendation: {movie[random_num]}")
    
print("Welcome to Movie reccomendation System")
print("Here are the movies for you:")
display_Data()

genres = movies_df['Genre'].unique()
genre = input(f"Please enter the genre from the following list: {', '.join(genres)}: ")
filter_data_on_genre(genre)

min_ratings = movies_df['Rating'].unique()
min_rating = float(input("Please enter the rating through which we can filter out: "))
filter_data_on_ratings(min_rating)
get_avg_ratings_of_films()
while(True):
    movie = input("Would you Like a random movie Selection from the list: ")
    if(movie == "Yes"):
        get_random_movie_selection()
    elif(movie == "No"):
        print("Thanks for using the software")
        break
    else:
        print("Invalid Input")
sys.exit()    
