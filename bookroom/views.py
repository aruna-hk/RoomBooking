from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .forms import RoomBookFilterModel
from .models import Room
import json

def index(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = RoomBookFilterModel()
            context = {}
            context['form'] = form
            purpose = request.GET.get('purpose', None)
            if purpose:
                context['purpose'] = purpose
                _rooms = Room.objects.filter(room_purpose=purpose).filter(room_available=True).values()
                print(_rooms)
                rooms = {}
                for room in _rooms:
                  rooms[str(room["id"])] = room
                print(rooms)
                return JsonResponse(rooms)
            return render(request, "home2.html", context)
    return redirect('login')

@csrf_exempt
def book(request):
    if request.user.is_authenticated:
        return redirect('Mpesa')
    else:
        return ('not logged in')

class About(TemplateView):
    template_name = "about.html"


