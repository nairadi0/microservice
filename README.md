# Find Zipcode coordinates microservice
SETUP
This Python script fetches the latitude and longitude of a given ZIP code using the Nominatim API from OpenStreetMap. It sends an HTTP request and returns the coordinates in JSON format.
1. dowload requests library

USAGE: 
Call the get_coordinates function with a valid ZIP code as the input.
The function will return the latitude and longitude in JSON format.

![image](https://github.com/user-attachments/assets/11f37544-8b99-4c82-99ac-1f6aeac07167)

EXAMPLE INPUT: 
zipcode = "10001"

EXAMPLE OUTPUT
print(f"Coordinates for ZIP code {zipcode}: {coordinates}")
![image](https://github.com/user-attachments/assets/1ba7cfdd-cf5d-482a-8d39-76a8e3881c69)

example output: Coordinates for ZIP code 10001: (40.712776, -74.005974)
![image](https://github.com/user-attachments/assets/22d63f2d-db03-4223-91e2-db4f48dbccc0)

