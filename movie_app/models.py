from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100, default='NoName')
    last_name = models.CharField(max_length=100, default='NoName')
    director_email = models.EmailField(default='sugar_daddy@gmail.com')
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
        return reverse('director_detail', args=[self.slug])


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DressingRoom(models.Model):
    floor = models.IntegerField(default=None)
    number = models.IntegerField(default=None)

    def __str__(self):
        return f'{self.floor} {self.number}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100, default='NoName')
    last_name = models.CharField(max_length=100, default='NoName')
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    slug = models.SlugField(default='', null=False, db_index=True)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        return f'Актриса {self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('actor_detail', args=[self.slug])


class Movie(models.Model):
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'
    CURRENCY_CHOICES = [
        (RUB, 'Rubles'),
        (EUR, 'Euro'),
        (USD, 'Dollars'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)], default=50)
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'

# from movie_app.models import Movie
# python manage.py shell_plus --print-sql
