from django.shortcuts import render
from consoles.models import Console

def index(request):
    context = { "consoles": Console.objects.all().order_by("name") }
    return render(request, "consoles/index.html", context)
