from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.db.utils import IntegrityError

from .models import Film, Category, Country
from mainapp.parsing import Parser


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
    def get(self, request: WSGIRequest, *args, **kwargs):
        filters = {
            'country': request.GET.get('country', None),
            'category': request.GET.get('category', None)
        }

        return render(request, 'catalog.html', self.prepare_context(filters))

    def prepare_context(self, filters=None):
        categories = Category.objects.all()
        countries = Country.objects.all()
        films = self.prepare_films(filters)

        context = {
            'categories': categories,
            'countries': countries,
            'films': films
        }

        return context

    def prepare_films(self, filters):
        country = filters['country']
        category = filters['category']

        if not country and not category:
            return Film.objects.all()

        films = Film.objects.all().filter()


class HelpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'help.html', self.prepare_context())

    def prepare_context(self):
        return {}


class FilmCreationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'film_creation_page.html', {})

    def post(self, request: WSGIRequest, *args, **kwargs):
        parser = Parser(request.POST['url'])

        try:
            parser.get_film_data()
        except IntegrityError as error:
            print(error)

        return HttpResponseRedirect('/film_creation/')
