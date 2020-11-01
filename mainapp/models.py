from django.db import models


class FilmManager:
    pass


class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name='Film Title')
    image = models.ImageField(verbose_name='Image')
    slug = models.SlugField(unique=True)

    description = models.TextField(max_length=1000, verbose_name='Film description', null=True, blank=True)
    full_hd = models.BooleanField(default=True)
    actors = models.ManyToManyField('Actor', verbose_name='Actors', null=True, blank=True)
    year = models.CharField(max_length=10)
    rating = models.CharField(max_length=10)
    lasting = models.CharField(max_length=10)

    countries = models.ManyToManyField('Country', verbose_name='Country', blank=True, null=True)
    categories = models.ManyToManyField('Category', verbose_name='Category', blank=True, null=True)

    constraints = models.CharField(max_length=10, verbose_name='Constraints', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_film_url(self):
        return f'films/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category Name')
    slug = models.SlugField(verbose_name='Category slug', unique=True)
    films = models.ManyToManyField('Film', verbose_name='Films', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_category_url(self):
        return f'genre/{self.name}/'


class Actor(models.Model):
    films = models.ManyToManyField('Film', verbose_name='Films', blank=True, null=True)

    biography = models.TextField(max_length=1000, verbose_name='Actor biography', null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='Actor country')
    first_name = models.CharField(max_length=255, default='Max')
    second_name = models.CharField(max_length=255, default='Brance')

    def __str__(self):
        return f'{self.first_name} - {self.second_name}'


class Country(models.Model):
    name = models.CharField(max_length=255)
    films = models.ManyToManyField('Film', verbose_name='Films', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_category_url(self):
        return f'country/{self.name}/'

