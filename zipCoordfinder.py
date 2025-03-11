
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, resources={r"/get-coordinates": {"origins": "*"}}) 

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
@app.route("/get-coordinates", methods=["GET"])
def get_zip_coordinates():
    zipcode = request.args.get("zipcode")
    if not zipcode:
        return jsonify({"error": "ZIP code is required"}), 400

    coordinates = get_coordinates(zipcode)
    return jsonify(coordinates)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
