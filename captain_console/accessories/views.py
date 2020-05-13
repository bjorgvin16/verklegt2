from django.shortcuts import render, get_object_or_404
from accessories.models import Accessory
from datetime import datetime
from frontpage.models import Manufacturer
from users.models import ProductView
from helpers.views import buildContext

def index(request):
    context = buildContext()
    context["manufacturer"] = Manufacturer.objects.all().order_by("name")
    context["accessories"] = Accessory.objects.all().order_by("name")
    return render(request, "accessories/index.html", context)

def get_console_by_id(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Accessory, pk=id)
        productview = ProductView.objects.filter(user=request.user, product=product)
        if not productview.exists():
            newrow = ProductView(user=request.user, product=product, dateOfView=datetime.now())
            newrow.save()
            print("hello")
        else:
            productview.update(dateOfView=datetime.now())
            print(datetime.now())
    context = buildContext()
    context["accessory"] = get_object_or_404(Accessory, pk=id)
    return render(request, "accessories/accessory_details.html", context)

def order_by_desc(request):
    context = buildContext()
    context["accessories"] = Accessory.objects.all().order_by("-name")
    return render(request, "accessories/index.html", context)

def order_by_highest_lowest(request):
    context = buildContext()
    context["accessories"] = Accessory.objects.all().order_by("-price")
    return render(request, "accessories/index.html", context)

def order_by_lowest_highest(request):
    context = buildContext()
    context["accessories"] = Accessory.objects.all().order_by("price")
    return render(request, "accessories/index.html", context)