from django.urls import path
from .views import Bank, Mpesa

urlpatterns = [
    path('mpesa/', Mpesa, name='Mpesa'),
    path('bank/', Bank, name='bank'),
]

