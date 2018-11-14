import webbrowser

class Movie():

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # a função __init__ cria espaço na memoria para title, storyline etc.

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # abrir o browser com a aplicação
        webbrowser.open(self.trailer_youtube_url)
