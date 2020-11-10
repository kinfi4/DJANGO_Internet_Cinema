from django.shortcuts import render
from django.views import View

from .models import Film, Category, Country


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', self.prepare_context())

    def prepare_context(self):
        films_top_rating = Film.objects.all().filter(is_released=True).order_by('-rating')[:6]
        films_new_release = Film.objects.all().filter(is_released=True)[:6]

        context = {
            'films_new_release': films_new_release,
            'films_top_rating': films_top_rating
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


class CatalogView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'catalog.html', self.prepare_context())

    def prepare_context(self):
        categories = Category.objects.all()
        countries = Country.objects.all()

        context = {
            'categories': categories,
            'countries': countries
        }

        return context


class HelpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'help.html', self.prepare_context())

    def prepare_context(self):
        return {}
