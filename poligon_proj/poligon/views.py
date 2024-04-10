from django.shortcuts import render
from django.contrib.gis import geos

from shapely.geometry import Polygon

from .forms import PolygonForm


def create_polygon(request):
    """Main view of create poligon."""
    form = PolygonForm(
            request.POST or None,
        )
    if request.method == 'POST':
        if form.is_valid():
            polygon = form.save(commit=False)
            polygon_antimeredian = str_to_polygon(request.POST.get('polygon'))
            polygon.area = polygon_antimeredian[0]
            form.save(commit=False).antimeredian = polygon_antimeredian[1]
            form.save()
    return render(
        request,
        'polygon/create_polygon.html',
        {'form': form}
    )


def str_to_polygon(str_polygon: str) -> list[geos.GEOSGeometry, bool]:
    """Make string values to PolygonField."""
    list_coordinates: list = str_polygon.split(' ')
    coordinates_polygon: list[tuple] = get_list_of_tuples(list_coordinates)
    polygon_obj: list[Polygon, bool] = get_polygon_obj(coordinates_polygon)
    return [geos.GEOSGeometry(polygon_obj[0].wkt, srid='4326'), polygon_obj[1]]


def get_list_of_tuples(coordinates_polygon: list[tuple]) -> list[tuple]:
    """Make a list into a list of tuples."""
    list_of_tuples_coord: list = []
    i: int = 1
    while True:
        try:
            list_of_tuples_coord.append((
                float(coordinates_polygon[i]),
                float(coordinates_polygon[i+1])
            ))
            i += 2
        except IndexError:
            break
    list_of_tuples_coord.append((
        float(coordinates_polygon[1]),
        float(coordinates_polygon[2])
    ))
    return list_of_tuples_coord


def get_polygon_obj(coordinates_polygon: list[tuple]) -> list[Polygon, bool]:
    """Get Polygon object."""
    coordinates_polygon: list[list, bool] = check_antimeredian(
        coordinates_polygon
    )
    return [Polygon(coordinates_polygon[0]), coordinates_polygon[1]]


def check_antimeredian(coordinates_polygon: list[tuple]) -> list[list, bool]:
    """Check coordinates for antimeredian."""
    if any(
        coordinates[1] < -180 or coordinates[1] > 180
        for coordinates in coordinates_polygon
    ):
        return [
            [(point[0], point[1] - 180) for point in coordinates_polygon],
            True
        ]
    return [coordinates_polygon, False]
