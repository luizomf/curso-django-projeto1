from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz Otávio',
    })
