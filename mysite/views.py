from django.shortcuts import render
from places.models import Place

def show_main_page(request):
    title = ["Легенды Москвы", "Крыши24.рф"]
    place_id = ['moscow_legends', 'roofs24']
    coordinates = {
        'moscow_legends': [37.64912239999976, 55.77754550000014],
        'roofs24': [37.32478399999957, 55.70731600000015]
    }


    data = {'title': title,
            'place_id': place_id,
            'coordinates': coordinates}



    return render(request, 'main_page.html', context=data)


