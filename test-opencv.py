import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create an empty image (black image)
emt_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)

# Print the shape of the image
print("Image Shape:", emt_img.shape)

# Display the image using matplotlib
plt.imshow(emt_img)
plt.title("Empty Image")
plt.show()
