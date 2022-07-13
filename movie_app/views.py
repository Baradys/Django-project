from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Avg, Value


# Create your views here.


def show_all_movie(request):
    movies = Movie.objects.annotate()
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'))
    return render(request, 'movie_app/all_movies.html', {
        "movies": movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        "movie": movie
    })


def show_all_directors(request):
    directors = Director.objects.annotate()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors
    })


def show_one_director(request, slug_director: str):
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })


def show_all_actors(request):
    actors = Actor.objects.annotate()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors
    })


def show_one_actor(request, slug_actor: str):
    actor = get_object_or_404(Actor, slug=slug_actor)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })
