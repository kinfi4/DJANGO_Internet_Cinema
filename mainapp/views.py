from django.shortcuts import render
from django.views import View

from .models import Film, Category


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', self.prepare_context())

    def prepare_context(self):
        films = Film.objects.all()

        context = {
            'films': films
        }

        return context


class FilmView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'film_detail.html', self.prepare_context(kwargs.get('film_slug')))

    def prepare_context(self, slug):
        context = {
            'film': Film.objects.get(slug=slug)
        }
        return context
