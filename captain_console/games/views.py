from django.shortcuts import render, get_object_or_404
from games.models import Game, Genre
from frontpage.models import Manufacturer
from users.models import ProductView
from helpers.views import buildContext
from datetime import datetime

def index(request):
    context = buildContext()
    context["games"] = Game.objects.all().order_by("name")
    return render(request, "games/index.html", context)

def get_game_by_id(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Game, pk=id)
        productview = ProductView.objects.filter(user=request.user, product=product)
        if not productview.exists():
            newrow = ProductView(user=request.user, product=product, dateOfView=datetime.now())
            newrow.save()
        else:
            productview.update(dateOfView=datetime.now())
    context = buildContext()
    context["game"] = get_object_or_404(Game, pk=id)

    genres = Game.genre.through.objects.filter(game_id=id)
    genre_list = []
    for genre in genres:
        name = Genre.objects.get(id=genre.genre_id)
        genre_list.append(name)
    context["genres"] = genre_list

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