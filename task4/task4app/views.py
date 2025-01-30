from django.shortcuts import render
from django.views.generic import TemplateView


def menu_page(request):
    return render(request, 'menu.html')

# def index(request):
#     return render(request, 'index.html')


def games(request):
    games = [
        'Atomic Heart',
        'Cyberpunk 2077',
        'PayDay'
    ]
    context = {'games': games}
    return render(request, 'games.html', context)

def korzinka(request):
    return render(request, 'korzinka.html')



