from frontpage.models import Manufacturer

def buildContext():
    return {"manufacturers": Manufacturer.objects.all().order_by("name")}