from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HTML(TemplateView):
    template_name = 'html.html'

class Favorite(TemplateView):
    template_name = 'favorite.html'

class Fruits(TemplateView):
    template_name = 'fruits.html'
    