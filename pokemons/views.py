from django.http import HttpResponse
from django.template import loader
from .models import Pokemon


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def pokemons(request):
    all_pokemon = Pokemon.objects.all().values()
    template = loader.get_template('pokedex.html')
    context = {
        'pokemons': all_pokemon,
    }
    return HttpResponse(template.render(context, request))


def details(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('details.html')
    context = {
        'pokemon': pokemon,
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry']
    }
    return HttpResponse(template.render(context, request))
