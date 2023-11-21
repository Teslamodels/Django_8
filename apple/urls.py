from django.urls import path
from .views import HTML, Fruits, Favorite

urlpatterns = [
    path('', HTML.as_view(), name='html'),
    path('fruits/', Fruits.as_view(), name='fruits'),
    path('favorite/', Favorite.as_view(), name='favorite'),
    
]