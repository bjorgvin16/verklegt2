from django.shortcuts import render, get_object_or_404
from games.models import Game

from frontpage.models import Manufacturer
from helpers.views import buildContext


def index(request):
    context = buildContext()
    #context = { "games": Game.objects.all().order_by("name") }
    context["games"] = Game.objects.all().order_by("name")
    return render(request, "games/index.html", context)

def get_game_by_id(request, id):
    context = {"game": get_object_or_404(Game, pk=id)}
    return render(request, "games/game_details.html", context)

def order_by_desc(request):
    context = {"games": Game.objects.all().order_by("-name")}
    return render(request, "games/index.html", context)

def order_by_highest_lowest(request):
    context = {"games": Game.objects.all().order_by("-price")}
    return render(request, "games/index.html", context)

def order_by_lowest_highest(request):
    context = {"games": Game.objects.all().order_by("price")}
    return render(request, "games/index.html", context)

def get_manufacturer_by_id(request, manufacturerid):
    games = Game.objects.filter(manufacturer_id=manufacturerid)
    manufacturer = Manufacturer.objects.filter(id = manufacturerid)
    context = {"games":games, "manufacturer":manufacturer}
    return render(request, 'games/games_by_manufacturer.html', context)