from django.shortcuts import render, get_object_or_404
from consoles.models import Console

from frontpage.models import Manufacturer
from helpers.views import buildContext

def index(request):
    context = buildContext()
    context["consoles"] = Console.objects.all().order_by("name")
    return render(request, "consoles/index.html", context)

def get_console_by_id(request, id):
    context = buildContext()
    context["consoles"] = get_object_or_404(Console, pk=id)
    return render(request, "consoles/console_details.html", context)

def order_by_desc(request):
    context = buildContext()
    context["consoles"] = Console.objects.all().order_by("-name")
    return render(request, "consoles/index.html", context)

def order_by_highest_lowest(request):
    context = buildContext()
    context["consoles"] = Console.objects.all().order_by("-price")
    return render(request, "consoles/index.html", context)

def order_by_lowest_highest(request):
    context = buildContext()
    context["consoles"] = Console.objects.all().order_by("price")
    return render(request, "consoles/index.html", context)

def get_manufacturer_by_id(request, manufacturerid):
    context = buildContext()
    context["consoles"] = Console.objects.filter(manufacturer_id=manufacturerid)
    context["manufacturer"] = Manufacturer.objects.get(id=manufacturerid)
    return render(request, 'consoles/consoles_by_manufacturer.html', context)