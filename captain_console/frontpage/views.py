from django.shortcuts import render
#from cart import Order
from users.models import ProductView
from helpers.views import buildContext
from consoles.models import Console
from games.models import Game

def index(request):
    context = buildContext()
    if request.user.is_authenticated:
        context["views"] = ProductView.objects.filter(user=request.user)
    context["consoles"] = Console.objects.all().order_by("-created_date")
    context["game"] = Game.objects.all()
    return render(request, 'frontpage/index.html', context)