#!/usr/bin/env python
import numpy as np
import heapq
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from PIL  import Image, ImageDraw, ImageColor

# Define the cost of moving from one pixel to another.
# We set the cost to 1 for adjacent pixels and sqrt(2) for diagonal pixels.
MOVE_COSTS = np.array([[np.sqrt(2), 1, np.sqrt(2)], [1, 0, 1], [np.sqrt(2), 1, np.sqrt(2)]])

class ShortestPathFinder:
    def __init__(self):
        # Load the binary map from file.

        binary_map = Image.open('mini_map_real2.png').convert('L')
        black_map = np.array(binary_map) < 10
        binary_map = np.array(binary_map) > 0
        if binary_map is not None:
            self.binary_map = binary_map > 0
            self.black_map = black_map
        else:
            rospy.logerr('Failed to load the binary map from file.')
            exit()

        # Define the size of the binary map.
        self.height, self.width = self.binary_map.shape[:2]

        # Create a 2D array of nodes, where each node has a cost and a parent.
        self.nodes = np.full((self.height, self.width), fill_value=np.array([(np.inf, None)], dtype=[('cost', float), ('parent', object)]))

        # Define a priority queue for the nodes to be visited by Dijkstra algorithm.
        self.pq = []

    def find_shortest_path(self, start, goal):
        """
        Find the shortest path between start and goal on a binary map using Dijkstra algorithm.

        Parameters:
            start (tuple): The starting pixel coordinates (y, x).
            goal (tuple): The goal pixel coordinates (y, x).

        Returns:
            path (list): A list of pixel coordinates that represent the shortest path from start to goal.
        """
        # Add the start node to the priority queue.
        self.nodes[start]['cost'] = 0
        heapq.heappush(self.pq, (0, start))

        # Define a function to get the neighbors of a pixel.
        def get_neighbors(pixel):
            y, x = pixel
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == dx == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width and self.binary_map[ny, nx] and not self.black_map[ny, nx]:
                        yield (ny, nx), (dy, dx)

        # Run Dijkstra algorithm.
        while self.pq:
            current_cost, current_pixel = heapq.heappop(self.pq)
            if current_pixel == goal:
                break
            for neighbor_pixel, (dy, dx) in get_neighbors(current_pixel):
                new_cost = self.nodes[current_pixel]['cost'] + MOVE_COSTS[1 + dy, 1 + dx]
                if new_cost < self.nodes[neighbor_pixel]['cost']:
                    self.nodes[neighbor_pixel]['cost'] = new_cost
                    self.nodes[neighbor_pixel]['parent'] = current_pixel
                    heapq.heappush(self.pq, (new_cost, neighbor_pixel))

        # Reconstruct the path from the goal node to the start node.
        path = []
        current_pixel = goal
        while current_pixel is not None:
            path.append(current_pixel)
            current_pixel = self.nodes[current_pixel]['parent']
        path.reverse()

        return path
def main():
    # Initialize the node.
    rospy.init_node('shortest_path_planner', anonymous=True)
    # Define the start and goal pixels.
    start = (555, 171)
    goal = (291, 252)

    # Find the shortest path between the start and goal pixels.
    spf = ShortestPathFinder()
    path = spf.find_shortest_path(start, goal)

    # Draw the path on the map.
    if len(path) > 0:
        # Load the map image
        map_img = Image.open('mini_map_real2.png').convert('RGB')

        # Create a new image for the path
        path_img = Image.new('RGB', map_img.size, color=(255, 255, 255))

        # Create a new ImageDraw object
        draw = ImageDraw.Draw(path_img)

        # Draw the path on the path image
        for i in range(len(path) - 1):
            draw.line([path[i][::-1], path[i + 1][::-1]], fill=ImageColor.getrgb('red'), width=2)

        # Blend the path image with the map image
        blended_img = Image.blend(map_img, path_img, alpha=0.5)

        # Display the blended image
        blended_img.show()
    else:
        rospy.logerr('Error: the binary map is empty.')
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass