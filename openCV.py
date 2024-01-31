import cv2
import numpy as np

# Replace 'path_to_image.jpg' with your image file
image = cv2.imread('/Users/seb/Documents/raceCar.png')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Finding contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Convert the image to HSV format
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color thresholds
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_green = np.array([36, 50, 50])
upper_green = np.array([86, 255, 255])
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

for cnt in contours:
    # Approximate the contour
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    # Draw the contour
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 5)

    # Identify shape
    vertices = len(approx)
    if vertices == 3:
        shape = "Triangle"
    elif vertices == 4:
        shape = "Rectangle"
    elif vertices > 4:
        shape = "Circle"
    elif vertices < 3:
        shape = "Line"
    elif vertices == 0:
        shape = "Point"
    elif vertices == 5:
        shape = "Pentagon"
    elif vertices == 6:
        shape = "Hexagon"
    else:
        shape = "Unknown"

    
  

   # Create a mask of the same size as the image, but single-channel (grayscale)
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [cnt], -1, 255, -1)  # Fill the contour with white (255)

    # Get the mean color of the shape
    mean = cv2.mean(hsv, mask=mask)

    # Identify color
    if lower_red[0] <= mean[0] <= upper_red[0]:
        color = "Red"
    elif lower_green[0] <= mean[0] <= upper_green[0]:
        color = "Green"
    elif lower_blue[0] <= mean[0] <= upper_blue[0]:
        color = "Blue"
    else:
        color = "Unknown"

    
    # Draw shape name and color with offset
    cv2.putText(image, f"{shape}, {color}", (approx[0][0][0], approx[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)



cv2.imshow('Shapes and Colors Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


