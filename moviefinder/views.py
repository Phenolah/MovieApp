from django.shortcuts import render
from tmdbv3api import TMDb, Movie
import requests
# Create your views here.

def home(request):
    tmdb = TMDb()
    tmdb.api_key = "bf16466eb69228572e21d716920bdd88"
    tmdb.language = 'en'
    tmdb.debug = True
    movie = Movie()
    recommendations = movie.recommendations(movie_id=111)

    for recommendation in recommendations:
        print(recommendation.id)
        print(recommendation.title)
        print(recommendation.overview)
        print(recommendation.poster_path)
    return render(request, 'movie.html')

