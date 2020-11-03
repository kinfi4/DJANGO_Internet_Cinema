from django.urls import path

from .views import BaseView, FilmView, CatalogView, HelpView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('films/<str:film_slug>/', FilmView.as_view(), name='film_detail'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('help/', HelpView.as_view(), name='help'),
]
