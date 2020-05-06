from django.shortcuts import render
from consoles.models import Console

def index(request):
    return render(request, "consoles/index.html", context={"consoles": Console.objects.all()})
