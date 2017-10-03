import webbrowser

class Movie():
    '''This class provides a way to store movie related information.'''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating, release_date):
        '''This function initializes the instance variables and makes room in memory when they are used'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.release_date = release_date

    def show_trailer(self):
        '''This function opens a youtube trailer in the browser'''
        webbrowser.open(self.trailer_youtube_url)
