import object_segmentation as lib
from PIL import Image, ImageDraw

path = input('Enter image path: ')
#gesture_x, gesture_y = int(input('Enter gesture coordinates: '))

image: Image = Image.open(path)
image = lib.set_monotone(image)
print("Done set_monotone")
image = lib.gaussian_blur(image)
print("Done gaussian_blur")
image = lib.calculate_gradient(image)
print("Done calculate_gradient")
image = lib.suppression_of_non_maxima(image, 8)
print("Done suppression_of_non_maxima")

image.show()
