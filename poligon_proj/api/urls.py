from rest_framework import routers
from django.urls import path, include

from .views import PolygonViewSet


router = routers.DefaultRouter()
router.register('polygon', PolygonViewSet, basename='polygon')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
