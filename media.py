import sys
import urllib
import json

class Movie():

    def __init__(self, title):
        self.title = title
        self.youtube_trailer_link = self.get_youtube_link(title)
        self.poster_url = self.get_poster_url(title)
        self.omdb_api_string = self.format_title(title)

#TODO: move the link formatting logic from html_gen to here
    def get_youtube_link(self, title):
        movie_data = self.get_movie_data(title)
        youtube_link = movie_data["youtube"]
        return youtube_link

    def get_poster_url(self, title):
        movie_data = self.get_movie_data(title)
        poster_url = movie_data["poster"]
        return poster_url

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
        print("Trailer: " + self.youtube_trailer_link)
        print("API String: " + self.omdb_api_string)






            # retrieves movie information from the Open Movie Data Base in JSON format
            # # See: https://www.omdbapi.com/ for more information on the API
            # def get_json(self, request):
            #     try:
            #         #if(DEBUG):
            #             #raise Exception, 'False network error: Testing local'
            #         url = "http://www.omdbapi.com/?t="+request+"&y=&plot=short&r=json"
            #         response = urllib.urlopen(url)
            #         movie_data = json.loads(response.read())
            #
            #     except: # Use a local backup file
            #         print("Unable to load " + request +
            #               " from www.omdbapi.com, using local mock data")
            #         mock = open("json_mock.json")
            #         data = json.loads(mock.read())
            #         mock.close()
            #         movie_data = data["the+empire+strikes+back"]
            #     return movie_data
