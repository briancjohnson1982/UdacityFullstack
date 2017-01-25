"""This module creates a website that features information about
some of my favorite movies.

"""
__author__ = 'Brian Johnson'
__version__ = '0.1'
__date__ = "Jan. 25, 2017"
__email__ = "briancjohnson1982@gmail.com"

import media
import html_gen

movie_titles = ["The Empire Strikes Back", "The Godfather",
                "The Princess Bride", "Casablanca", "Dead Poets Society",
                "Akira", "Office Space", "The Matrix", "Fight Club"]

# Create an array of movie objects
movies = []
for title in movie_titles:
    movie = media.Movie(title)
    movies.append(movie)

# Send array to html_gen to create the html file
html_gen.open_movies_page(movies)
