#!/usr/bin/env python3

import rospy
from PIL import Image, ImageTk
import requests
from tkinter import messagebox
import math
import tkinter as tk
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import Point
from my_message.msg import Start_and_Goal

# Get the radius of the Earth in meters
earth_radius = 6378137 
# Get the value of pi
pi = math.pi
# Replace YOUR_API_KEY with your actual API key
api_key = "AIzaSyCBeB575UrWUFwrCxdRvTFiyVPHzxihGGk"

# Set the desired zoom level and dimensions for the mini map
zoom_level = 18
width = 601
height = 601
pixels_per_degree = 256 * pow(2, zoom_level) / 360
degrees_per_pixel = 1/pixels_per_degree

# Determine the center of the map and then the 4 corners
center_lat, center_lng = 10.881714, 106.809030
center_x, center_y=300, 300

# Build the URL for the Google Static Maps API
url = f"https://maps.googleapis.com/maps/api/staticmap?center={center_lat},{center_lng}&size={width}x{height}&zoom={zoom_level}&maptype=roadmap&style=feature:all|element:labels|visibility:off"

# Add your API key to the URL
url += f"&key={api_key}"

# Download the image from the URL
response = requests.get(url)
with open("mini_map.png", "wb") as f:
    f.write(response.content)
class MapApp:
    def __init__(self, master):
        self.point_msg = Start_and_Goal()
        self.master = master
        self.master.title("Mini Map")
        self.point = Start_and_Goal()
        # Load the image into a Tkinter PhotoImage object
        self.image = ImageTk.PhotoImage(Image.open("mini_map.png"))

        # Create a Canvas widget to display the image
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.canvas.pack()

        # Bind a callback function to the left-click event on the canvas
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Subscribe to the GPS coordinates of the robot
        rospy.Subscriber('gps', NavSatFix, self.on_gps_update)

        # Publish the start and goal point
        self.pub = rospy.Publisher('/points', Start_and_Goal, queue_size= 10)
        self.pub.publish(self.point_msg)

    def on_canvas_click(self, event):
        # Get the X and Y coordinates of the mouse click
        x = event.x
        y = event.y

        # Convert the pixel coordinates to latitude and longitude
        lat = center_lat - (y-center_y)*degrees_per_pixel 
        lng = center_lng + (x-center_x)*degrees_per_pixel 

        # Display the coordinates in a message box
        message = f"Latitude: {lat:.6f}\nLongitude: {lng:.6f}\nx:{x}\ny:{y}"
        tk.messagebox.showinfo("Coordinates", message)
        self.point_msg.robot_x = x
        self.point_msg.robot_y = y
    def on_gps_update(self, gps_msg):
        # Get the latitude and longitude from the NavSatFix message
        lat = gps_msg.latitude
        lng = gps_msg.longitude
        # Remove the last red dot, if it exists
        if hasattr(self, 'last_dot'):
            self.canvas.delete(self.last_dot)
        # Convert the latitude and longitude to pixel coordinates
        x = int((lng - center_lng) * pixels_per_degree + center_x)
        y = int((center_lat - lat) * pixels_per_degree + center_y)

        # Draw a red dot at the robot's position
        self.last_dot = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill='red', outline='red')
        self.point_msg.clicked_x = x
        self.point_msg.clicked_y = y
def main():
    rospy.init_node("mini_map")

    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()