from django.shortcuts import render

# Create your views here.
from .models import *
from .forms import ReserveTableForm

def reserve_table(request):
    reserve_form = ReserveTableForm()
    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            reserve_form = ReserveTableForm()

    context = {
        'form' : reserve_form
    }
    return render(request, 'Reservation/reservation.html', context)
