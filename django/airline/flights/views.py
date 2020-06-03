from django.http import Http404
from django.shortcuts import render
from .models import Flight


# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)


def flight(req, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404('Flight does not exist.')

    context = {
        'flight': flight
    }
    return render(req, 'flights/flight.html', context)

