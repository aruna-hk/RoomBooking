from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_dict = {}
        for key, value in request.POST.items():
            if key == 'csrfmiddlewaretoken':
                continue
            if key == 'password1' or key == 'password2':
                user_dict['password'] = value
            else:
                user_dict[key] = value
        if form.is_valid():
            user = User.objects.create_user(**user_dict)
            return redirect('login')
        return render(request, 'register.html', {"form": form})

    form = UserCreationForm()
    return render(request, "register.html", {"form": form})

