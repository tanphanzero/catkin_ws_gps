import tkinter as tk
from PIL import Image, ImageTk
import requests
from tkinter import messagebox
import math

# Get the radius of the Earth in meters
earth_radius = 6378137 
# Get the value of pi
pi = math.pi
# Replace YOUR_API_KEY with your actual API key
api_key = "AIzaSyCBeB575UrWUFwrCxdRvTFiyVPHzxihGGk"

# Set the desired zoom level and dimensions for the mini map
zoom_level = 20
width = 601
height = 601
pixels_per_degree = 256 * pow(2, zoom_level) / 360
degrees_per_pixel = 1/pixels_per_degree

# Determine the center of the map and then the 4 corner
#center_lat, center_lng = 10.881714, 106.809030
center_lat, center_lng = 10.87973483, 106.80578267
center_x, center_y=300, 300

# Build the URL for the Google Static Maps API
url = f"https://maps.googleapis.com/maps/api/staticmap?center={center_lat},{center_lng}&size={width}x{height}&zoom={zoom_level}&maptype=roadmap&style=feature:all|element:labels|visibility:off"



# Add your API key to the URL
url += f"&key={api_key}"

# Download the image from the URL
response = requests.get(url)
with open("mini_map_real.png", "wb") as f:
    f.write(response.content)

class MapApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mini Map")

        # Load the image into a Tkinter PhotoImage object
        self.image = ImageTk.PhotoImage(Image.open("mini_map_real.png"))

        # Create a Canvas widget to display the image
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.canvas.pack()

        # Bind a callback function to the left-click event on the canvas
        self.canvas.bind("<Button-1>", self.on_canvas_click)

   
    def on_canvas_click(self, event):
        # Get the X and Y coordinates of the mouse click
        x = event.x
        y = event.y

        # Convert the pixel coordinates to latitude and longitude
        lat = center_lat - (y-center_y)*degrees_per_pixel 
        lng = center_lng + (x-center_x)*degrees_per_pixel 

        # Display the coordinates in a message box
        #message = f"Latitude: {lat:.6f}\nLongitude: {lng:.6f}\nx:{x}\ny:{y}"
        #tk.messagebox.showinfo("Coordinates", message)    
root = tk.Tk()
app = MapApp(root)
while True:
    lat = float(input('lat'))
    lng = float(input('long'))
    def lat_lng_to_pixel(lat, lng):
        # Get the delta between the center latitude and the given latitude
        y = center_y + (center_lat - lat) / degrees_per_pixel

        # Get the delta between the given longitude and the center longitude
        x = center_x + (lng - center_lng) / degrees_per_pixel


        # Return the pixel coordinates as a tuple
        return (int(x), int(y))
    pixel = lat_lng_to_pixel(lat,lng)
    print('x and y =', pixel )
    print('meters per pixel =', degrees_per_pixel*111000)