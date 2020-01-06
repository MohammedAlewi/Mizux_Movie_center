from django.db import models

class Movie:
    def __init__(self,movie_title,movie_description,main_star,released_date):
        self.movie_title= movie_title
        self.movie_description = movie_description
        self.main_star = main_star
        self.released_date = released_date


class MovieCategory:
    def __init__(self,category_name,description,movie_genere,movies=None):
        self.movies= movies
        self.category_name = category_name
        self.description = description
        self.genere = movie_genere



