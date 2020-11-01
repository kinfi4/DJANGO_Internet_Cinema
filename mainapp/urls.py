from django.urls import path

from .views import BaseView, FilmView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('films/<str:film_slug>/', FilmView.as_view(), name='film_detail')
]