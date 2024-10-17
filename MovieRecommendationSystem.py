import pandas as pd
import numpy as np
import sys
import random
import matplotlib.pyplot as plt

# Data
data = {
    'Title': [
        'Inception', 'The Dark Knight', 'Titanic', 'Avatar', 'The Matrix',
        'Interstellar', 'The Avengers', 'The Godfather', 'Jurassic Park', 'Pulp Fiction',
        'The Shawshank Redemption', 'Forrest Gump', 'Gladiator', 'The Lord of the Rings: The Return of the King',
        'Star Wars: Episode IV - A New Hope', 'Fight Club', 'The Lion King', 'The Silence of the Lambs',
        'The Departed', 'Schindler\'s List', 'The Room', 'Cats', 'Gigli', 'Battlefield Earth', 'Dragonball Evolution'
    ],
    'Genre': [
        'Sci-Fi', 'Action', 'Romance', 'Sci-Fi', 'Sci-Fi',
        'Sci-Fi', 'Action', 'Crime', 'Adventure', 'Crime',
        'Drama', 'Drama', 'Action', 'Adventure',
        'Sci-Fi', 'Drama', 'Animation', 'Thriller',
        'Crime', 'Biography', 'Drama', 'Musical', 'Romance', 'Sci-Fi', 'Action'
    ],
    'Rating': [
        4.8, 4.9, 4.7, 4.6, 4.5,
        4.7, 4.5, 4.9, 4.6, 4.8,
        4.9, 4.8, 4.7, 4.9,
        4.8, 4.7, 4.9, 4.8,
        4.7, 4.9, 2.0, 1.5, 2.3, 2.1, 1.8
    ],
    'ReleaseYear': [
        2010, 2008, 1997, 2009, 1999,
        2014, 2012, 1972, 1993, 1994,
        1994, 1994, 2000, 2003,
        1977, 1999, 1994, 1991,
        2006, 1993, 2003, 2019, 2003, 2000, 2009
    ],
    'Popularity': [
        12000, 15000, 13000, 14000, 9000,
        13000, 16000, 11000, 9000, 10500,
        15000, 14000, 12500, 16000,
        13500, 12000, 16000, 10000,
        11500, 11000, 2000, 1500, 2500, 1800, 1300
    ]
}

# Create DataFrame
movies_df = pd.DataFrame(data)

# Function to improve DataFrame display options
def set_pandas_display_options():
    pd.set_option('display.max_columns', None)  # Ensure all columns are shown
    pd.set_option('display.width', 1000)  # Set the display width to 1000 to avoid cutting off
    pd.set_option('display.max_rows', None)  # Display all rows if needed

# Display full DataFrame
def display_Data():
    set_pandas_display_options()
    print(movies_df)

# Filter data by genre
def filter_data_on_genre(genre):
    print(movies_df[movies_df['Genre'] == genre])

# Filter data by rating
def filter_data_on_ratings(min_rating):
    print("Here is the filtered data:")
    print(movies_df[movies_df['Rating'] >= min_rating])

# Get average rating of all movies
def get_avg_ratings_of_films():
    print(f"Average movie rating: {movies_df['Rating'].mean()}")

# Get a random movie recommendation
def get_random_movie_selection():
    length = len(movies_df)
    random_num = random.randint(0, length - 1)
    movie = np.array(movies_df['Title'])
    print(f"Random movie recommendation: {movie[random_num]}")

# Display a bar plot of movie ratings
def displayBarPlot():
    x = np.array(movies_df['Title'])
    y = np.array(movies_df['Rating'])
    plt.figure(figsize=(10, 7))  # Set figure size to avoid overlap in plot
    plt.bar(x, y)
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.xlabel("Movie Names")
    plt.title("Movies with Ratings")
    plt.ylabel("Ratings")
    plt.show()

# Start of the Movie Recommendation System
print("Welcome to the Movie Recommendation System")
print("Here are the movies for you:")
display_Data()

# Ask user if they want graphical output
graph = input("Would you like a graphical format? Enter Yes or No: ")
if graph.lower() == "yes": 
    displayBarPlot()

# Filter by genre
genres = movies_df['Genre'].unique()
genre = input(f"Please enter the genre from the following list: {', '.join(genres)}: ")
filter_data_on_genre(genre)

# Filter by minimum rating
min_rating = float(input("Please enter the minimum rating to filter movies: "))
filter_data_on_ratings(min_rating)

# Show average ratings
get_avg_ratings_of_films()

# Random movie selection loop
while True:
    movie = input("Would you like a random movie selection from the list? (Yes/No): ")
    if movie.lower() == "yes":
        get_random_movie_selection()
    elif movie.lower() == "no":
        print("Thanks for using the software!")
        break
    else:
        print("Invalid Input")

sys.exit()
