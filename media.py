import webbrowser

class Movie:
    """  Movies have string fields for the four main attributes of a movie,
    name, plot, trailer (either on youtube or not), poster image on harddrive

    Attributes:
        str1, title, or the name of the movie in string
        str2, storyline, a brief description of what the movi is about.
        str3, trailer link, youtube link that can be embedded within html and
            also played esternally
        str4, poster, path to a local file that has the poster image so that
            the html file can display it for the user to click on and view the
            trailer
    """
    def __init__(self, name, description, trailer, poster):
        """  This is the constructor, memory is initialized in this function
        right here  """
        self.title = name
        self.storyline = description
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster

    def play_trailer(self):
        """  This class meathod plays the trailer of the movie on a webbrowser.
        It uses the webbrowser python library and opens it in the default
        webbrowser  """
        webbrowser.open(self.youtube_trailer)
