from django.contrib import admin
from .models import Movie


# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status']
    list_editable = ['rating', 'year', 'budget']
    ordering = ['-rating', 'name']
    list_per_page = 10

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Ну такое себе'
        if movie.rating < 70:
            return 'Можно глянуть'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'
