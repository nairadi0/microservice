# Find Zipcode coordinates microservice

This Python script fetches the latitude and longitude of a given ZIP code using the Nominatim API from OpenStreetMap. It sends an HTTP request and returns the coordinates in JSON format.
1. dowload requests library
2. download script
3. example inpit: zipcode = "97006"
coordinates = get_coordinates(zipcode)
print(f"Coordinates for ZIP code {zipcode}: {coordinates}")

example output: Coordinates for ZIP code 10001: (40.712776, -74.005974)
![image](https://github.com/user-attachments/assets/22d63f2d-db03-4223-91e2-db4f48dbccc0)

