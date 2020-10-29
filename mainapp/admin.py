from django.contrib import admin
# from django.contrib.sites import

from .models import *

admin.site.register(Film)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Country)
