from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from poligon.models import Polygon
from poligon.views import str_to_polygon
from .serializers import (
    PolygonSerializer,
    PolygonSerializerUpdateObj
)


class PolygonViewSet(ModelViewSet):
    """CRUD object of Polygon."""

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return PolygonSerializerUpdateObj
        return PolygonSerializer
    queryset = Polygon.objects.all()

    def create(self, request):
        area = str_to_polygon(request.data.get('area'))
        polygon = PolygonSerializer(
            data={
                'name': request.data.get('name'),
                'area': area[0],
                'antimeridian': area[1]
            },
            context={'request': request},
        )
        polygon.is_valid(raise_exception=True)
        polygon.save()
        return Response(
            polygon.data,
            status=status.HTTP_201_CREATED
        )
