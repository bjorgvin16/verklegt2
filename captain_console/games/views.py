from django.shortcuts import render

game = [
    {'name': 'Super Mario Bros 2',
     'price': 4000,
     'description': 'Mario is back and better than ever in a new Super Mario Bros 2 full of exiting new levels.',
     'genre': 'action, adventure',
     'publisher': 'Nintendo',
     'releaseyear': '1988',
     'platform': 'NES, Wii, Nintendo 3DS...'
     },
    {'name': 'The Legend of Zelda: Ocarina of Time',
     'price': 4000,
     'description': 'Link, a young warrior sets off on an adventure of a lifetime',
     'genre': 'action, adventure',
     'publisher': 'Nintendo',
     'releaseyear': 1998,
     'platform': 'Nintendo 64, Wii, Nintendo DS...'
     }
]

def index(request):
    return render(request, 'games/index.html', context={
        'game': game
    })