from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Place
# Create your views here.
def show_place_page(request, post_id):
    place =get_object_or_404(Place, id=post_id)
    return HttpResponse(place.title)