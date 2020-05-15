from accessories.models import Accessory
from consoles.models import Console
from frontpage.models import Manufacturer
from games.models import Game


def buildContext():
    return {"manufacturers": Manufacturer.objects.all().order_by("name")}

def findTypeFromId(productid):
    games = Game.objects.all()

    for game in games:
        if game.id == productid:
            return "game"

    accessories = Accessory.objects.all()

    for accessory in accessories:
        if accessory.id == productid:
            return "accessory"

    consoles = Console.objects.all()

    for console in consoles:
        if console.id == productid:
            return "console"