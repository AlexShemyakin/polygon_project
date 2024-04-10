from django.contrib.gis.db import models

from .constants import MAX_LENGTH_TEXT_FIELD, MAX_LENGTH_AREA_FIELD


class Polygon(models.Model):
    """Polygon."""
    name = models.CharField(
        'Название',
        max_length=MAX_LENGTH_TEXT_FIELD,
        unique=True
    )
    area = models.PolygonField(
        'Широта и долгота.',
        max_length=MAX_LENGTH_AREA_FIELD,
        blank=True,
    )
    antimeridian = models.BooleanField(
        'Пересечение меридиана.',
    )

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name
