import numpy as np
import cv2

# Black image
black = np.zeros([150, 200, 1], 'uint8') # single channel image, no RGB, just black or white
cv2.imshow("Black", black)
# slice notation, [<row>, <column>, <channel>], we use ":" to indicate when we want all values of the parameter specified
# to print out the pixel value at the origin
print(black[0,0,:])

# Technically not black, but since one is a very low number compared to 255, it looks black to us
ones = np.ones([150,200,3], 'uint8')
cv2.imshow("Ones", ones)
print(ones[0,0,:])

# Making a white image
white = np.ones([150, 200, 3], 'uint16') # we will see that the max size of any type of array is white
# black to white scales with the data type used in the array of each pixel
white *= (2**16 -1) # subtract 1 because we start at 0
cv2.imshow("White", white)
print(white[0,0,:])

# making a blue image
color = ones.copy() # creates a deep copy, not connected to the other object
color[:, :] = (255, 0, 0) # setting all pixels, i.e, from all heights and all widths to (255, 0, 0)
## NOTE: the color space in openCV is BGR, so (255, 0, 0) is blue, not red
cv2.imshow("Color", color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()