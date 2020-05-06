from django.shortcuts import render
from games.models import Game

def index(request):
    context = { 'games': Game.objects.all().order_by('name') }
    return render(request, 'games/index.html', context)