from django.shortcuts import render
from users.models import ProductView
from helpers.views import buildContext
from consoles.models import Console
from games.models import Game
from accessories.models import Accessory
from .models import Product

def index(request):
    context = buildContext()
    if request.user.is_authenticated:
        context["productviews"] = ProductView.objects.filter(user=request.user).order_by("-dateOfView")

    context["consoles"] = Console.objects.all().order_by("-dateAdded")
    context["games"] = Game.objects.all().order_by("-dateAdded")
    context["accessories"] = Accessory.objects.all().order_by("-dateAdded")
    return render(request, 'frontpage/index.html', context)

def get_all_products(request):
    context = buildContext()
    context["products"] = Product.objects.filter(display=True).order_by("name")
    context["games"] = Game.objects.filter(display=True)
    context["consoles"] = Console.objects.filter(display=True)
    context["accessories"] = Accessory.objects.filter(display=True)
    return render(request, 'frontpage/all_products.html', context)

def order_by_desc(request):
    context = buildContext()
    context["products"] = Product.objects.filter(display=True).order_by("name")
    context["games"] = Game.objects.filter(display=True).order_by("-name")
    context["consoles"] = Console.objects.filter(display=True).order_by("-name")
    context["accessories"] = Accessory.objects.filter(display=True).order_by("-name")
    return render(request, "frontpage/all_products.html", context)

def order_by_highest_lowest(request):
    context = buildContext()
    context["products"] = Product.objects.filter(display=True).order_by("-price")
    context["games"] = Game.objects.filter(display=True).order_by("-price")
    context["consoles"] = Console.objects.filter(display=True).order_by("-price")
    context["accessories"] = Accessory.objects.filter(display=True).order_by("-price")
    return render(request, "frontpage/all_products.html", context)

def order_by_lowest_highest(request):
    context = buildContext()
    context["products"] = Product.objects.filter(display=True).order_by("price")
    context["games"] = Game.objects.filter(display=True).order_by("price")
    context["consoles"] = Console.objects.filter(display=True).order_by("price")
    context["accessories"] = Accessory.objects.filter(display=True).order_by("price")
    return render(request, "frontpage/all_products.html", context)