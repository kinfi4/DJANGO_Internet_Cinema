import requests
import sys

from io import BytesIO

from bs4 import BeautifulSoup
from PIL import Image
from django.core.files.images import ImageFile
from django.db.models import QuerySet

from mainapp.models import Film, Category, Country
from mainapp.utils.slug_creator import create_slug


class Parser:
    WEB_HOST = 'https://gidonline.io'

    def __init__(self, url):
        self.url = url
        html = requests.get(url).content
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_film_data(self):
        title = self.soup.find('h1', {'itemprop': 'name'}).text
        slug = self.url.split('/')[-2]
        year = self.soup.find('div', {'itemprop': 'dateCreated'}).find('a').text

        country_tags = self.soup.find('div', {'itemprop': 'countryOfOrigin'}).find_all('a')
        country_names = [country_tag.text.replace(',', '') for country_tag in country_tags]
        countries = []

        for country_name in country_names:
            try:
                countries.append(Country.objects.get(name=country_name))
            except Exception as ex:
                sl = create_slug(country_name.lower())
                print(sl)
                country = Country.objects.create(name=country_name, slug=sl)
                countries.append(country)

        genre_tags = self.soup.find('div', {'itemprop': 'genre'}).find_all('a')
        genre_names = [genre_tag.text.replace(',', '') for genre_tag in genre_tags]
        genres = []

        print(genre_names)
        for category_name in genre_names:
            try:
                genres.append(Category.objects.get(name=category_name))
            except Exception as ex:
                sl = create_slug(category_name.lower())
                print(sl)
                genre = Category.objects.create(name=category_name, slug=sl)
                genres.append(genre)

        lasting = self.soup.find('div', {'itemprop': 'duration'}).text
        constraints = self.soup.find('div', class_='t-row').find_all('div', class_='r-2')[2].find_all('a')[-1].text
        description = self.soup.find('div', {'itemprop': 'description'}).find('p').text

        image_src = self.soup.find('img', {'class': 't-img'}).attrs['src']
        img = requests.get(self.WEB_HOST + image_src).content

        rating = float(self.soup.find('div', {'class': 'ratings-score'}).text.split()[-1])

        film = Film.objects.create(title=title, slug=slug, year=year, description=description, rating=rating,
                                   lasting=lasting, constraints=constraints,
                                   image=ImageFile(BytesIO(img), name=slug + '.jpg'))

        film.countries.add(*countries)
        film.categories.add(*genres)
        film.save()
