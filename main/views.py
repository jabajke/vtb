from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Вы находитесь на главной странице',
        'content': 'Слева есть меню навигации по сайту'
    }

    return render(request, 'index.html', context)


def geographical(request):
    title = GeographicPosition.objects.filter().first().title
    content = GeographicPosition.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'geographic.html', context)


def economic_dev(request):
    title = EconomicDevelopment.objects.filter().first().title
    content = EconomicDevelopment.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'economicdev.html', context)


def export(request):
    title = Export.objects.filter().first().title
    content = Export.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'export.html', context)


def nature(request):
    title = Nature.objects.filter().first().title
    content = Nature.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'nature.html', context)


def ecological(request):
    title = EcologicalCondition.objects.filter().first().title
    content = EcologicalCondition.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'ecological.html', context)


def biography(request):
    title = FamousBiologistAndGeographist.objects.filter().first().title
    content = FamousBiologistAndGeographist.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'famous.html', context)


def short_history(request):
    title = ShortHistoricalFacts.objects.filter().first().title
    content = ShortHistoricalFacts.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'shorthistory.html', context)


def memory(request):
    title = MemorablePlaces.objects.filter().first().title
    content = MemorablePlaces.objects.filter().first().content
    context = {'title': title, 'content': content}

    return render(request, 'memorable.html', context)
