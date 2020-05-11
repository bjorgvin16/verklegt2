from django.shortcuts import render, get_object_or_404
from consoles.models import Console

def index(request):
    context = { "consoles": Console.objects.all().order_by("name") }
    return render(request, "consoles/index.html", context)

def get_console_by_id(request, id):
    context = {"console": get_object_or_404(Console, pk=id)}
    return render(request, "consoles/console_details.html", context)

def order_by_desc(request):
    context = { "consoles": Console.objects.all().order_by("-name") }
    return render(request, "consoles/index.html", context)

def order_by_highest_lowest(request):
    context = {"consoles": Console.objects.all().order_by("-price")}
    return render(request, "consoles/index.html", context)

def order_by_lowest_highest(request):
    context = {"consoles": Console.objects.all().order_by("price")}
    return render(request, "consoles/index.html", context)