#Contains a set of classes related to media such as movies

class Movie():
    '''Class that contains general information about a movie.
        Formatted in such a way that it can be called by the
        fresh_tomatoes.py file and thus dispalyed in the html file'''

    #init file to gather all the information called by theme
    #create_movie_tiles_content function in fresh_tomatoes.py
    def __init__(self, movie_title, movie_poster_url, movie_trailer_url, movie_id):
        self.title = movie_title
        self.poster_image_url = movie_poster_url #link to an image file
        self.trailer_youtube_url = movie_trailer_url #link to a trailer on youtube
        self.movie_id = movie_id

    #give this a readable name so people know what it is if its printed
    def __str__(self):
        name_string = "Movie Object with information about {}".format(self.title)
        return name_string

    #give it a callable name
    def __repr__(self):
        return self.movie_id
