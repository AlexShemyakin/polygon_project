from rest_framework import serializers

from poligon.models import Polygon
from poligon.views import str_to_polygon


class PolygonSerializer(serializers.ModelSerializer):
    """Serializers create object of Polygon."""

    class Meta:
        model = Polygon
        fields = ('pk', 'name', 'area', 'antimeridian')


class PolygonSerializerUpdateObj(serializers.ModelSerializer):
    """Serializers update object of Polygon."""

    class Meta:
        model = Polygon
        fields = ('name', 'area', 'antimeridian',)

    def update(self, instance, validated_data):
        """Update object of Polygon."""
        name = validated_data.pop('name')
        area = str_to_polygon(validated_data.pop('area'))
        instance.name = name
        instance.area = area[0]
        instance.antimeridian = area[1]
        instance.save()
        return instance
