from django.shortcuts import render
from frontpage.models import Product
from games.models import Game
from accessories.models import Accessory
from consoles.models import Console
from helpers.views import buildContext

def index(request):
    context = buildContext()

    search = request.GET.get('search', None)
    if search:
        context["products"] = Product.objects.filter(name__icontains=search)
        context["games"] = Game.objects.all()
        context["accessories"] = Accessory.objects.all()
        context["consoles"] = Console.objects.all()
        context["search"] = search

    return render(request, 'productsearch/index.html', context)