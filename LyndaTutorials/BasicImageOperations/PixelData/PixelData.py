import numpy as np
import cv2

img = cv2.imread("opencv-logo.png", 1) 
# 1 - use default colors and channels provided with the image
# 0 - image in black and white

#============== Show pixel data ==================
print("What is img?")
print(img)

# show data type of image
print("Data type of img: ", end="")
print(type(img))

#==== note: we're actually working with np.ndarray objects here ======

# Now we'll dive into pixel information
## if we run the following code, we can see that there are xxx rows in the image, This indicates that there are xxx pixels in each column
print("Number of pixels in outer layer OR height of image (in pixels): ", end="")
print(len(img))

## going further in, we can also view how many pixels there are in each row
print("Number of pixels in each row OR number width of image (in pixels): ", end="")
print(len(img[0]))

## lastly, we can check the number of channels in the image by going in by one more level
print("Number of channels: ", end="")
print(len(img[0][0]))

## all of these information can be summarized or attained easily with the shape variable
print("From shape method: ", end="")
print(img.shape)

## finding the data type of the pixels
print("Data type of pixels: ", end="")
print(img.dtype) # we will see that it is an uint8, which means that there are 2**8 possible values for each pixel
# uint8 is an 8 bit integer. range of values from 0 to 255

## at this point, we can access individual pixels
print("Pixel values at the 10th row, 5th column: ", end="")
print(img[10, 5]) # 10th row, 5th column

## We can also access individual channel 
print("One channel image: ", end="")
print(img[:, :, 0]) # 0 for first channel, 1 and 2 for next two channels

## finally, we can find the total pixel size of the image
print("Total pixels in this image: ", end="")
print(img.size)