from django.shortcuts import render, HttpResponse
from tmdbv3api import TMDb, Movie
from .forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import DetailView, ListView
from .models import *
from django.contrib.auth.decorators import login_required
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
    return render(request, 'home.html')'''

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
    return render(request, 'home.html', context)



#Categorize movies based on genres
def movie_by_genres(request):
    context = {}
    return render(request, context)

@login_required()
def watchlist(request):
    context = {}
    return render(request, context)

@login_required
def rating(request):
    context = {}
    return render(request, context)

@login_required
def want_to_watch(request):
    context = {}
    return render(request, context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Wrong credentials. Try again.')
                return redirect('login')
        else:
            form = UserLoginForm()
            context = {
               "form": form,
            }
            return render(request, 'login.html', context)

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Hi {username}, your account was successfully created')
                return redirect('login')
        else:
            form = UserRegistrationForm()
            context = {'fields': form}
            return render(request, 'registration.html', context)


def logout(request):
    return render(request, 'logout.html')

class MoviedetailView(ListView):
    model = MovieDetails
    template_name = 'moviedetails.html'
