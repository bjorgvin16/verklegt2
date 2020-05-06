from django.shortcuts import render, get_object_or_404
from accessories.models import Accessory

def index(request):
    context = { "accessories": Accessory.objects.all().order_by("name") }
    return render(request, "accessories/index.html", context)

def get_console_by_id(request, id):
    context = {"accessory": get_object_or_404(Accessory, pk=id)}
    return render(request, "accessories/accessory_details.html", context)