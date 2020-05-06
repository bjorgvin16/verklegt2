from django.shortcuts import render
from consoles.models import Console

def index(request):
    context = {"consoles": Console.objects.all()}
    return render(request, "consoles/index.html")
