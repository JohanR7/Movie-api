from django.urls import path
from . import views

urlpatterns = [
    path('popular/', views.popular_movies, name="popular-movies"),
    path('top-rated/', views.top_rated_movies, name="top-rated-movies"),
    path('search/', views.search_movies, name="search-movies"),
    path('now-playing/',views.now_playing,name="now-playing"),
    path('upcoming/',views.upcoming,name="upcoming-movies"),
    path('filter/',views.filter,name="filter-movies"),
    path('compare/',views.compare,name="compare-movies"),
]
