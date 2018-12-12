import webbrowser

class Movie():
    # Este cria a classe de atributos e comportamentos

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
      # Esta função será usada para fazer uma instância. Os argumentos serão"
        "armazenados dentro de métodos que serão usados pelos objetos.

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Esta função é responsavel para abrir o Trailer
        webbrowser.open(self.trailer_youtube_url)
