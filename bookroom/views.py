from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

from .forms import RoomBookFilterModel
from .models import Room

def index(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = RoomBookFilterModel()
            context = {}
            context['form'] = form
            purpose = request.GET.get('room_purpose', None)
            if purpose:
                context['purpose'] = purpose
                rooms = Room.objects.filter(room_purpose=purpose)
                context['rooms'] = rooms
                print("------")
                print(rooms)
                print("------")
            return render(request, 'home.html', context)
    return redirect('login')

class About(TemplateView):
    template_name = "about.html"


