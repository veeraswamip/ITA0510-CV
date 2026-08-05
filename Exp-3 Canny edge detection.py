import cv2

# Read the input image
image = cv2.imread("sample.jpg")   # Image must be in same folder

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray_image, 100, 200)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", edges)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
