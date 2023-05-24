from . import views
from django.urls import path

urlpatterns = [
    path('movies/', views.movie_by_genre, name='home'),
    path('search/', views.search, name='search'),
]
