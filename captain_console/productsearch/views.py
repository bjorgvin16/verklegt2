from django.shortcuts import render
from frontpage.models import Product
from games.models import Game
from accessories.models import Accessory
from consoles.models import Console
from django.http import JsonResponse

# Create your views here.
def index(request):
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
    context = {
        "products": Product.objects.filter(name__icontains=search) ,
        "games": Game.objects.all(),
        "accessories": Accessory.objects.all(),
        "consoles": Console.objects.all(),
    }
    return render(request, 'productsearch/index.html', context)