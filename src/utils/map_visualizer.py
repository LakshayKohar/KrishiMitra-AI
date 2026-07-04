import geemap
import ee


def create_ndvi_map(ndvi_image, latitude, longitude):
    """
    Create an interactive NDVI map.
    """

    Map = geemap.Map(center=[latitude, longitude], zoom=14)

    ndvi_params = {
        "min": -1,
        "max": 1,
        "palette": [
            "red",
            "yellow",
            "green"
        ]
    }

    Map.addLayer(ndvi_image, ndvi_params, "NDVI")

    Map.add_marker([latitude, longitude], popup="Selected Location")

    return Map