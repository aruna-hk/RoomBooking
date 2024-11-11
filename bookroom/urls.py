from django.urls import path
from .views import index, About#, book_room
urlpatterns = [
#    path('roombookin/', book_room, name='book'),
    path('', index, name='home'),
    path('about/', About.as_view(), name='about'),
]

