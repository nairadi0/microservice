import requests

def get_coordinates(zipcode, country="US"):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "postalcode": zipcode,
        "country": country,
        "format": "json"
    }
    headers = {
        "User-Agent": "ZipLookup/1.0"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return float(lat), float(lon)
        else:
            return "No results found"
    else:
        return f"Error: {response.status_code}"

# Example usage
zipcode = "97006"
coordinates = get_coordinates(zipcode)
print(f"Coordinates for ZIP code {zipcode}: {coordinates}")
