import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "AIzaSyCBeB575UrWUFwrCxdRvTFiyVPHzxihGGk"

# Set the desired zoom level and dimensions for the mini map
zoom_level = 17
width = 400
height = 400

# Build the URL for the Google Static Maps API
url = f"https://maps.googleapis.com/maps/api/staticmap?size={width}x{height}&zoom={zoom_level}&maptype=roadmap"

# Add markers for the four corners of the rectangle
lat1, lng1 = 10.882573944236247, 106.80893898346855
lat2, lng2 = 10.881977176150635, 106.80999587807236
lat3, lng3 = 10.881023674620808, 106.80792253045401
lat4, lng4 = 10.88039415123081, 106.80896590979224

markers = [
    f"markers=color:red%7Clabel:A%7C{lat1},{lng1}",
    f"markers=color:red%7Clabel:B%7C{lat2},{lng2}",
    f"markers=color:red%7Clabel:C%7C{lat3},{lng3}",
    f"markers=color:red%7Clabel:D%7C{lat4},{lng4}"
]

# Set the bounds of the mini-map to the four corners of the rectangle
bounds = f"{lat1},{lng1}|{lat2},{lng2}|{lat3},{lng3}|{lat4},{lng4}"
url += f"&markers={bounds}"

# Add your API key to the URL
url += f"&key={api_key}"

# Download the image from the URL
response = requests.get(url)
with open("mini_map.png", "wb") as f:
    f.write(response.content)
