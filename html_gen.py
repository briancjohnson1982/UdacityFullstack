import webbrowser
import os


# This file is based on ... TODO: finish heaer comments

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Movies</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="css/styles.css" media ="screen">


    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="javascript/movie_player_scripts.js"></script>

</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
            <div class="left-column col-lg-4">
                <div class="trailer-title-bar">
                    <h2></h2>
                </div>
                <div class="trailer-side-bar">

                    <div id="plot-summary">
                        <h3>Plot Summary:</h3>
                        <div id="plot">
                        </div>
                    </div>
                    <hr>
                    <div id="people">
                        <h3>People:</h3>

                        <span><h4>Writen By:</h4><span id="writer"></span></span>
                        <span><h4>Directed By:</h4><span id="director"></span></span>
                        <span><h4>Starring:</h4><span id="starring"></span></span>
                    </div>
                </div>
            </div> <!-- END SIDE COLUMN -->
            <div class="right-column col-lg-8">
                  <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                  </a>
                  <div class="scale-media" id="trailer-video-container">
                  </div>
                  <div class="lower-trailer-bar">
                      <h3>lowerBar</h3>
                  </div>

            </div> <!-- END RIGHT COLUMN -->
        </div>
      </div>
    </div>  <!-- END VIDEO CONTAINER-->




    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-omdb-request-string ="{omdb_api_string}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" class="poster">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):

    # The HTML content for this section of the page
    content = ''
    for movie in movies:

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_url,
            omdb_api_string=movie.omdb_api_string,
            trailer_youtube_id= movie.trailer_youtube_id
        )

    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
