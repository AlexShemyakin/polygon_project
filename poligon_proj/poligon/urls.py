from django.urls import path

from .views import create_polygon


app_name = 'polygon'

urlpatterns = [
    path('', create_polygon, name='create_polygon')
]
