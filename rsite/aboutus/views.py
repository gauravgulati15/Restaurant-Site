from django.shortcuts import render

# Create your views here.
from .models import *

def aboutus_list(request):
    about         = AboutUs.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    chef          = Chef.objects.all()

    context = {
        'about'        : about,
        'why_choose_us': why_choose_us,
        'chef'         : chef,
    }

    return render(request, 'aboutus/about.html', context)
    