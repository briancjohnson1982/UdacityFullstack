import media
import html_gen

DEBUG = True;

movie_titles = ["The Empire Strikes Back", "The Godfather", "The Princess Bride",
"Casablanca", "Dead Poets Society", "Akira", "Office Space","The Matrix",
"Fight Club"]

# create an array of movie objects
movies = []
for title in movie_titles:
    movie = media.Movie(title)
    movies.append(movie)
    if(DEBUG):
        movie.print_info()


html_gen.open_movies_page(movies)
