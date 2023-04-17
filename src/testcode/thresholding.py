# import required libraries
import cv2

# load the input image
img = cv2.imread('mini_map.png')

# convert the input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding to convert grayscale to binary image
ret,thresh = cv2.threshold(gray,240,255,0)

# Display the Binary Image
cv2.imshow("Binary Image", thresh)
cv2.imwrite("mini_map1.png", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()