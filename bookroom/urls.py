from django.urls import path
from .views import index, About, book
urlpatterns = [
    path('book/', book, name='book'),
    path('about/', About.as_view(), name='about'),
    path('', index, name='home'),
]

