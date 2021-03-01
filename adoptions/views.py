from django.shortcuts import render
from django.http import Http404

# import the models for the views
from .models import Pet

# Create your views here.
def home(request):
    # query all the pets
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets': pets,
    })


def pet_detail(request, pet_id):
    # for this one need to use try and expect because if the id doesnt not exist python won't give errors
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {
        'pet':pet,
    })
