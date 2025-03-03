import requests

USER_AGENT = "ZipLookup/1.0"
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

def _fetch_coordinates_data(zipcode, country):
    params = {
        "postalcode": zipcode,
        "country": country,
        "format": "json"
    }
    headers = {
        "User-Agent": USER_AGENT
    }

    try:
        response = requests.get(NOMINATIM_URL, params=params, headers=headers)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None



