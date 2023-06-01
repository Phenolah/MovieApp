from . import views
from django.urls import path

urlpatterns = [
    path('', views.movie_by_genre, name='home'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),


]
