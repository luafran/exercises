
class Movie:
    def __init__(self, movie_id, rating):
        self.id = movie_id
        self.rating = rating
        self.related = {}

    def add_related(self, movie):
        if movie.id not in self.related:
            self.related[movie.id] = movie