from django.shortcuts import render
from frontpage.models import Product
from django.http import JsonResponse

def index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search) ]
        return JsonResponse({ 'data': products })
    return render(request, 'frontpage/index.html')