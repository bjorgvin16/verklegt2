from django.shortcuts import render
from frontpage.models import Product
from games.models import Game
from accessories.models import Accessory
from consoles.models import Console
from django.http import JsonResponse
from helpers.views import buildContext

# Create your views here.
def index(request):
    context = buildContext()
    '''
    if 'search' in request.GET:
        search = request.GET['search']
        context = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search) ]
        return JsonResponse({ 'data': products })

    if 'search' in request.GET:
        '''
    search = request.GET['search']
    context["products"] = Product.objects.filter(name__icontains=search)
    context["games"] = Game.objects.all()
    context["accessories"] = Accessory.objects.all()
    context["consoles"] = Console.objects.all()
    context["search"] = search

    return render(request, 'productsearch/index.html', context)