import sys
import urllib
import json
import re

class Movie():

    def __init__(self, title):
        self.title = title
        self.poster_url = self.get_poster_url(title)
        self.trailer_youtube_id = self.get_youtube_id(title)
        self.omdb_api_string = self.format_title(title)

    # get poster url from local file
    def get_poster_url(self, title):
        movie_data = self.get_movie_data(title)
        poster_url = movie_data["poster"]
        return poster_url

    # get youtube id from local file
    def get_youtube_id(self, title):
        movie_data = self.get_movie_data(title)
        trailer_youtube_url = movie_data["youtube"]
        trailer_youtube_id = self.extract_youtube_id(trailer_youtube_url)
        return trailer_youtube_id

    # moved this here from the main html generation file
    # Extract the youtube ID from the url
    def extract_youtube_id(self, trailer_youtube_url):
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        return trailer_youtube_id

    #get information about this title in json format from local file
    def get_movie_data(self, title):
        movie_file = open("movie_info.json")
        movie_data = json.loads(movie_file.read())
        movie_file.close()
        return movie_data[title]

    #format the title for use in client-side calls to the Open Movie Data Base
    # See: https://www.omdbapi.com/ for more information on the API
    def format_title(self, title):
        formatted_title = title.lower()
        title_words = formatted_title.split()
        separator = "+"
        formatted_title = separator.join(title_words)
        return formatted_title

    # printing function for testing
    def print_info(self):
        print("Title: " + self.title)
        print("Poster: "  + self.poster_url)
        print("Trailer ID: " + self.trailer_youtube_id)
        print("API String: " + self.omdb_api_string)
