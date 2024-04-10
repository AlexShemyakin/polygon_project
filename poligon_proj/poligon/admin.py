from django.contrib import admin

from .models import Polygon


@admin.register(Polygon)
class PolygonAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'area',
        'antimeridian',
    )

    search_fields = ('name',)
    list_filter = ('name',)
