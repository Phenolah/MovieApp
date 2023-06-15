from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.movie_by_genre, name='home'),
    path('login/', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
    path("change-password/", auth_views.PasswordChangeView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.logout, name='logout'),
    path('moviedetails/', views.MoviedetailView.as_view(), name='moviedetails' )

]
