from django.contrib import admin, messages
from .models import Movie, Director, Actor
from django.db.models import QuerySet


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 69', 'Средний'),
            ('>=70', 'Высокий')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 69':
            return queryset.filter(rating__gte=40).filter(rating__lt=70)
        if self.value() == '>=70':
            return queryset.filter(rating__gte=70)


@admin.register(Actor)
class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ['first_name', 'last_name']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ['first_name', 'last_name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['rating', 'name']
    # exclude = ['slug']
    # readonly_fields = ['slug']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'director', 'year', 'budget', 'rating_status', 'currency']
    list_editable = ['rating', 'year', 'director', 'budget', 'currency']
    filter_horizontal = ['actors']
    ordering = ['-rating', 'name']
    list_per_page = 10
    actions = ['set_dollars', 'set_rubles', 'set_euros']
    search_fields = ['name__startswith']
    list_filter = [RatingFilter]

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
