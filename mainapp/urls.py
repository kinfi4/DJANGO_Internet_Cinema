from django.urls import path

from .views import BaseView, FilmView, CatalogView, HelpView, FilmCreationView, FilmFindView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('films/<str:film_slug>/', FilmView.as_view(), name='film_detail'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('help/', HelpView.as_view(), name='help'),
    path('film_creation/', FilmCreationView.as_view(), name='film_creation'),
    path('film_find', FilmFindView.as_view(), name='film_find'),
]
