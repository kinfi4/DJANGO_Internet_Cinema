from django.shortcuts import render
from django.shortcuts import HttpResponse


def test(request):
    return render(request, 'base.html', {})
