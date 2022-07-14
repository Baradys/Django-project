from . import views
from django.urls import path


urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('directors/', views.DirectorsView.as_view()),
    path('directors/<slug>', views.DirectorDetail.as_view(), name='director_detail'),
    path('actors/', views.ActorsView.as_view()),
    path('actors/<slug>', views.ActorDetail.as_view(), name='actor_detail'),


]
