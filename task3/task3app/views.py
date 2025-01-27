from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def korzinka(request):
    return render(request, 'korzinka.html')


def games(request):
    title = 'Игры'
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay'
    context = {
        'title': title,
        'text1': game1,
        'text2': game2,
        'text3': game3
    }
    return render(request, 'games.html', context)


def index(request):

    text = 'Главная страница'
    context = {
        'text': text

    }
    return render(request, 'index.html', context)
