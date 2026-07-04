from geopy.geocoders import Nominatim


def get_coordinates(place_name):
    """
    Convert a place name into latitude and longitude.
    """

    geolocator = Nominatim(user_agent="krishimitra-ai")

    location = geolocator.geocode(place_name)

    if location is None:
        raise ValueError(f"Could not find location: {place_name}")

    return location.latitude, location.longitude