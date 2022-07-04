from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status', 'currency']
    list_editable = ['rating', 'year', 'budget', 'currency']
    ordering = ['-rating', 'name']
    list_per_page = 10
    actions = ['set_dollars', 'set_rubles', 'set_euros']

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Ну такое себе'
        if movie.rating < 70:
            return 'Можно глянуть'
        if movie.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.display(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        count_updates = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_updates} записей'
        )

    @admin.display(description='Установить валюту в рубль')
    def set_rubles(self, request, qs: QuerySet):
        count_updates = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_updates} записей'
        )

    @admin.display(description='Установить валюту в евро')
    def set_euros(self, request, qs: QuerySet):
        count_updates = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_updates} записей',
            messages.ERROR
        )
