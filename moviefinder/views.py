from django.shortcuts import render
from tmdbv3api import TMDb, Movie
import requests
# Create your views here.

'''def home(request):
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
    return render(request, 'movie.html')'''

import requests

url = "https://api.themoviedb.org/3/configuration/languages"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

def movie_by_genre(request, genre_id):
    # create an instance of TMDb
    tmdb = TMDb()
    #set the API key for TMDb
    tmdb.api_key = "5b53dca38bee489bbad4e8d7394d6438"
    #set the language for TMDb requests
    tmdb.language = 'en'
    # enable debug mode for TMDb
    tmdb.debug = True

    # create an instance for the movie class
    movie= Movie()
    #get the list of movies by genre using the genre ID
    movies = movie.discover_with_genres(genre_id)
    context = {'movies': movies}
    # render the template with the movies data
    return render(request, 'movie.html', context)
