import sys
import urllib
import json

class Movie():

    DEBUG = True
    
    def __init__(self, title_string, trailer_youtube_url):
        movie_data = self.get_json(title_string)
        self.title = movie_data["Title"]
        self.movie_plot = movie_data["Plot"]
        self.rating = movie_data["Rated"]
        self.release_date = movie_data["Released"]
        self.duration = movie_data["Runtime"]
        self.writer = movie_data["Writer"]
        self.director = movie_data["Director"]
        self.stars = movie_data["Actors"]
        self.poster_image_url = movie_data["Poster"]
        self.trailer_youtube_url = trailer_youtube_url
        

    # retrieves movie information from the Open Movie Data Base in JSON format
    # See: https://www.omdbapi.com/ for more information on the API
    def get_json(self, request):
        try:
            if(DEBUG):
                raise Exception, 'False network error: Testing local' 
            url = "http://www.omdbapi.com/?t="+request+"&y=&plot=short&r=json"
            response = urllib.urlopen(url)
            movie_data = json.loads(response.read())

        except: # Use a local backup file 
            print("Unable to load " + request +
                  " from www.omdbapi.com, using local mock data")
            mock = open("json_mock.json")
            data = json.loads(mock.read())
            mock.close()
            movie_data = data["the+empire+strikes+back"]
        return movie_data
            
    # test
    def print_info(self):
        print("Title: " + self.title)
        print("Plot: " + self.movie_plot)
        print("Rating: "  + self.rating)
        print("Released: "  + self.release_date)
        print("Duration: "  + self.duration)
        print("Written By: "  + self.writer)
        print("Directed By: "  + self.director)
        print("Starring: "  + self.stars)       
        print("Poster: "  + self.poster_image_url)
        print("Trailer: " + self.trailer_youtube_url)
        

        
