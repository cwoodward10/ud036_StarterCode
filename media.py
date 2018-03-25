#Contains a set of classes related to media such as movies

class Movie():
    '''Class that contains general information about a movie.

        The class is formatted in such a way that it can be called by the
        fresh_tomatoes.py file and thus dispalyed in the html file'''


    def __init__(self, movie_title, movie_poster_url, movie_trailer_url, movie_id):
        '''Inits class movie '''
        self.title = movie_title
        self.poster_image_url = movie_poster_url  #link to an image file
        self.trailer_youtube_url = movie_trailer_url  #link to a trailer on youtube
        self.movie_id = movie_id  #added so that a name can be dynamically assigned
                                  #when pulled from the  csv file

    def __str__(self):
        name_string = "Movie Object with information about {}".format(self.title)
        return name_string

    def __repr__(self):
        '''used so class can be dynamically named using movie_id'''
        return self.movie_id
