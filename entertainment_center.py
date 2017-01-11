import media
import html_gen

DEBUG = True;

movie_requests = [
    ["the+empire+strikes+back", "https://www.youtube.com/watch?v=xESiohGGP7g"], 
    ["the+godfather", "https://www.youtube.com/watch?v=sY1S34973zA"],
    ["the+princess+bride", "https://www.youtube.com/watch?v=VYgcrny2hRs"],
    ["casablanca", "https://www.youtube.com/watch?v=S9ID5DHsX8g"],
    ["dead+poets+society", "https://www.youtube.com/watch?v=wrBk780aOis"],
    ["akira", "https://www.youtube.com/watch?v=7G5zQW4TinQ"],
    ["office+space", "https://www.youtube.com/watch?v=dMIrlP61Z9s"],
    ["the+shawshank+redemption", "https://www.youtube.com/watch?v=NmzuHjWmXOc"],
    ["fight+club", "https://www.youtube.com/watch?v=SUXWAEX2jlg"],
    ["the+matrix", "https://www.youtube.com/watch?v=m8e-FF8MsqU"]]

movies = []
for request in movie_requests:   
    movie = media.Movie(request[0], request[1])
    movies.append(movie)
    if(DEBUG):
        movie.print_info()
	

html_gen.open_movies_page(movies)
