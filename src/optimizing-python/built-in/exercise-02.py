import skimage.io
import numpy as np

# loads the image
image = skimage.io.imread('https://i.imgur.com/gpLmzNk.png')
print('values in image:')
print(image)

# normalize the image by dividing each
# value by 255; store in variable named
# newImage
#newImage = image / 255
newImage = np.zeros(image.shape)

from timeit import default_timer as timer

startTime = timer()
for i in range(image.shape[0]):
  for j in range(image.shape[1]):
    for k in range(image.shape[2]):
      newImage[i][j][k] = image[i][j][k] / 255.0
stopTime = timer()

print('values in new image:')
print(newImage)

print(stopTime - startTime)