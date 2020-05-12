from frontpage.models import Manufacturer

def buildContext():
    return {"manufacturer": Manufacturer.objects.all().order_by("name")}