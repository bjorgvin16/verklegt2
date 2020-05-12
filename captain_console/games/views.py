from django.shortcuts import render, get_object_or_404
from games.models import Game

from frontpage.models import Manufacturer
from helpers.views import buildContext


def index(request):
    context = buildContext()
    context["games"] = Game.objects.all().order_by("name")
    return render(request, "games/index.html", context)

def get_game_by_id(request, id):
    context = buildContext()
    context["game"] = get_object_or_404(Game, pk=id)
    return render(request, "games/game_details.html", context)

def order_by_desc(request):
    context = buildContext()
    context["games"] = Game.objects.all().order_by("-name")
    return render(request, "games/index.html", context)

def order_by_highest_lowest(request):
    context = buildContext()
    context["games"] = Game.objects.all().order_by("-price")
    return render(request, "games/index.html", context)

def order_by_lowest_highest(request):
    context = buildContext()
    context["games"] = Game.objects.all().order_by("price")
    return render(request, "games/index.html", context)

def get_manufacturer_by_id(request, manufacturerid):
    context = buildContext()
    context["games"] = Game.objects.filter(manufacturer_id=manufacturerid)
    context["manufacturer"] = Manufacturer.objects.get(id=manufacturerid)
    return render(request, 'games/games_by_manufacturer.html', context)