
    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
        // keeping things consistent. Actually, it seems like there is probably
        // a better way to remove this information. Any feedback would be appreciated.
        $(".trailer-title-bar").empty();
        $("#plot").empty();
        $("#writer").empty();
        $("#director").empty();
        $("#starring").empty();

    });

    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '.movie-tile', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

        var omdbRequestString = $(this).attr('data-omdb-request-string');
        var omdbUrl = 'http://www.omdbapi.com/?t='+ omdbRequestString +'&y=&plot=short&r=json';

        jsonData = $.getJSON(omdbUrl, function(data){
            title = data["Title"];
            $(".trailer-title-bar").append("<h2>"+title+"</h2>");
            $("#plot").append(data["Plot"]);
            $("#writer").append(data["Writer"]);
            $("#director").append(data["Director"]);
            $("#starring").append(data["Actors"]);
            $(".lower-trailer-bar").append(data["Rated"] + " " + data["Runtime"] + " " + data["Released"]);
        });


        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
          'id': 'trailer-video',
          'type': 'text-html',
          'src': sourceUrl,
          'frameborder': 0
        }));
    });
    // Animate in the movies when the page loads
    $(document).ready(function () {
      $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
      });
    });
