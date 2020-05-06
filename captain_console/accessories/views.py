from django.shortcuts import render
from accessories.models import Accessory


def index(request):
    context = { "accessories": Accessory.objects.all().order_by("name") }
    return render(request, "accessories/index.html", context)