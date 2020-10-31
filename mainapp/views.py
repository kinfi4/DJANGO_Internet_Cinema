from django.shortcuts import render
from django.views import View

from .models import Film


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', self.prepare_context())

    def prepare_context(self):
        context = {
            'films': Film.objects.all()
        }

        return context
