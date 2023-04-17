import numpy as np
import heapq
import rospy
from PIL import Image, ImageDraw, ImageColor
# Define the cost of moving from one pixel to another.
# We set the cost to 1 for adjacent pixels and sqrt(2) for diagonal pixels.
import cv2
MOVE_COSTS = np.array([[np.sqrt(2), 1, np.sqrt(2)], [1, 0, 1], [np.sqrt(2), 1, np.sqrt(2)]])

def find_shortest_path(start, goal, binary_map):
    """
    Find the shortest path between start and goal on a binary map using Dijkstra algorithm.
    
    Parameters:
        start (tuple): The starting pixel coordinates (y, x).
        goal (tuple): The goal pixel coordinates (y, x).
        binary_map (numpy.ndarray): The binary map, where black pixels are obstacles and white pixels are free spaces.
        
    Returns:
        path (list): A list of pixel coordinates that represent the shortest path from start to goal.
    """
    # Define the size of the binary map.
    height, width = binary_map.shape[:2]

    # Create a 2D array of nodes, where each node has a cost and a parent.
    #nodes = np.full((height, width), fill_value=(np.inf, None), dtype=[('cost', float), ('parent', object)])
    nodes = np.full((height, width), fill_value=np.array([(np.inf, None)], dtype=[('cost', float), ('parent', object)]))

    # Define a priority queue for the nodes to be visited by Dijkstra algorithm.
    pq = []

    # Add the start node to the priority queue.
    nodes[start]['cost'] = 0
    heapq.heappush(pq, (0, start))

    # Define a function to get the neighbors of a pixel.
    def get_neighbors(pixel):
        y, x = pixel
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == dx == 0:
                    continue
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width and binary_map[ny, nx] and not black_map[ny, nx]:
                    yield (ny, nx), (dy, dx)

    # Run Dijkstra algorithm.
    while pq:
        current_cost, current_pixel = heapq.heappop(pq)
        if current_pixel == goal:
            break
        for neighbor_pixel, (dy, dx) in get_neighbors(current_pixel):
            new_cost = nodes[current_pixel]['cost'] + MOVE_COSTS[1 + dy, 1 + dx]
            if new_cost < nodes[neighbor_pixel]['cost']:
                nodes[neighbor_pixel]['cost'] = new_cost
                nodes[neighbor_pixel]['parent'] = current_pixel
                heapq.heappush(pq, (new_cost, neighbor_pixel))    
    # Reconstruct the path from the goal node to the start node.
    path = []
    current_pixel = goal
    while current_pixel is not None:
        path.append(current_pixel)
        current_pixel = nodes[current_pixel]['parent']
    path.reverse()

    return path

# Load the binary map from file.
binary_map = Image.open('mini_map_real2.png').convert('L')
black_map = np.array(binary_map) < 10
binary_map = np.array(binary_map) > 0
'''

binary_map = cv2.imread('mini_map1.png', cv2.IMREAD_GRAYSCALE)
black_map = binary_map <10
if binary_map is not None:
    binary_map = binary_map > 0
else:
    print('Error: failed to load the binary map from file.')
    exit()
'''
# Find the shortest path between two pixels.
start = (555, 171)
goal = (291, 252)
path = find_shortest_path(start, goal, binary_map)

# Draw the path on the map.
'''
if len(path) > 0:
    #map_with_path = cv2.cvtColor(binary_map.astype(np.uint8) * 255, cv2.COLOR_GRAY2RGB)
    map_with_path = cv2.imread('mini_map1.png')
    for i in range(len(path) - 1):
        cv2.line(map_with_path, path[i][::-1], path[i + 1][::-1], (0, 0, 255), thickness=2)

    # Display the map with the path.
    cv2.imwrite('mapwithpath.jpg', map_with_path)
    cv2.imshow('Map with Path', map_with_path)
    cv2.waitKey(0)

    # Keep the window open until the user closes it.
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close all windows.
    cv2.destroyAllWindows()
else:
    print('Error: the binary map is empty.')
'''

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
    print('Error: the binary map is empty.')

