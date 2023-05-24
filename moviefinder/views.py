from django.shortcuts import render, HttpResponse
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

def movie_by_genre(request):
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

    context = {'movies': movie}
    # render the template with the movies data
    return render(request, 'movie.html', context)\

def search(request):
    # Get the query from the search bar
    query = request.GET.get('q')

    # If the query is not empty
    if query:
        # API request URL based on the query and API key
        search_url = f"https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1&query={query}&api_key=5b53dca38bee489bbad4e8d7394d6438"

        # Make a request to the API and retrieve the search results
        response = requests.get(search_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Retrieve the search results from the response JSON
            search_results = response.json()
        else:
            # Handle API request error
            search_results = None

        context = {
            'results': search_results,
            'query': query
        }
    else:
        # If the query is empty, set search_results to None
        return HttpResponse("Please enter a search query")
        context = {}

    return render(request, 'search.html', context)
