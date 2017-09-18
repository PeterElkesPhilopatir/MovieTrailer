import webbrowser


class Movie():

    def __init__(self, title, story, poster_image_url, trailer_youtube_url):
        # to Construct the movie object
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def showTrailer(self):
        # it opens browser to show the link
        webbrowser.open(self.trailer)
