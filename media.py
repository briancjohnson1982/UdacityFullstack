import sys
import urllib
import json
import re


class Movie():

    """Create a movie object from its title.

    Args:
        title (str): the movie's title

    Attributes:
        title (str): the movie's title
        poster_url (str): a url to and image of the movie's poster
        trailer_youtube_id (str): the youtube id number for the movie's trailer
        omdb_api_string (str): the title formatted for use in client-side calls
        to the Open Movie Database. See: https://www.omdbapi.com/ for more
        information on the API

    """

    def __init__(self, title):
        self.title = title
        self.poster_url = self.get_poster_url(title)
        self.trailer_youtube_id = self.get_youtube_id(title)
        self.omdb_api_string = self.format_title(title)

    def get_poster_url(self, title):
        """Get poster url from local file"""
        movie_data = self.get_movie_data(title)
        poster_url = movie_data["poster"]
        return poster_url

    def get_youtube_id(self, title):
        """Get youtube id from local file"""
        movie_data = self.get_movie_data(title)
        trailer_youtube_url = movie_data["youtube"]
        trailer_youtube_id = self.extract_youtube_id(trailer_youtube_url)
        return trailer_youtube_id

    # This was moved from the main html generation file since other information
    # is being formatted here.
    def extract_youtube_id(self, trailer_youtube_url):
        """Extract youtube ID from the url"""
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        return trailer_youtube_id

    # Helper function for retrieving JSON data from a local file
    def get_movie_data(self, title):
        """Open JSON file and return contents"""
        movie_file = open("movie_info.json")
        movie_data = json.loads(movie_file.read())
        movie_file.close()
        return movie_data[title]

    def format_title(self, title):
        """Format the title for calls to the Open Movie Database API."""
        formatted_title = title.lower()
        title_words = formatted_title.split()
        separator = "+"
        formatted_title = separator.join(title_words)
        return formatted_title

    # Printing function for testing
    def print_info(self):
        """Print the object's member variables values"""
        print("Title: " + self.title)
        print("Poster: " + self.poster_url)
        print("Trailer ID: " + self.trailer_youtube_id)
        print("API String: " + self.omdb_api_string)
