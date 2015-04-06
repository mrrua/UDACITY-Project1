#initiation function of the class
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, imdb_link, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb = imdb_link
        self.release = release_date

        
    
