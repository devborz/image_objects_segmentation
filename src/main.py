from PIL import Image, ImageDraw
from math import sqrt

def set_monotone(image: Image):
    draw = ImageDraw.Draw(image)
    pix = image.load()
    width = image.size[0]
    height = image.size[1]
    for x in range(width):
        for y in range(height):
            r = g = b = int(0.299*pix[x, y][0] + 0.587*pix[x, y][1]
                + 0.114*pix[x, y][2])
            draw.point((x, y), (r, g, b))

    image.save("/Users/usman/Desktop/result2.jpg", "JPEG")
    return image

def gaussian_blur(image: Image):
    blured_image = image.copy()
    draw = ImageDraw.Draw(blured_image)
    pix = image.load()
    width = image.size[0]
    height = image.size[1]
    radius = 2
    for x in range(width):
        for y in range(height):
            x0 = x - radius if x - radius > 0 else 0
            xn = x + radius if x + radius < width else width - 1
            y0 = y - radius if y - radius > 0 else 0
            yn = y + radius if y + radius < height else height - 1
            sum = 0
            for i in range(x0, xn + 1):
                for j in range(y0, yn + 1):
                    sum += pix[x, y][0]
#print(x0, xn, y0, yn, 4 * (xn - x0 + 1) * (yn - y0 + 1))
            r = g = b = sum // (4*(xn - x0 + 1)*(yn - y0 + 1))
            draw.point((x, y), (r, g, b))
    return blured_image

def calculate_gradient(image: Image):
    x_grad_image = image.copy()
    y_grad_image = image.copy()
    grad_image = image.copy()
    draw = ImageDraw.Draw(grad_image)
    x_draw = ImageDraw.Draw(x_grad_image)
    y_draw = ImageDraw.Draw(y_grad_image)
    pix = image.load()
    width = image.size[0]
    height = image.size[1]
    x_grade = [[0] * width] * height
    x_grade = [[0] * width] * height
    for y in range(height):
        for x in range(1, width):
            r = g = b = abs(pix[x, y][0] - pix[x - 1, y][0])
            x_draw.point((x, y), (r, g, b))
    for x in range(width):
        for y in range(1, height):
            r = g = b = abs(pix[x, y][0] - pix[x, y - 1][0])
            y_draw.point((x, y), (r, g, b))
    x_pix = x_grad_image.load()
    y_pix = y_grad_image.load()
    for x in range(width):
        for y in range(height):
            r = g = b = int(sqrt(x_pix[x, y][0]**2 + y_pix[x, y][0]**2))
            draw.point((x, y), (r, g, b))
    return grad_image

def suppression_of_non_maxima(image: Image):
    return image

def select_obj(image: Image, gesture_x: int, gesture_y: int):
    return image


path = '/Users/usman/Desktop/' + input('Enter image path: ')
image: Image = Image.open(path)
new_image = set_monotone(image)
#new_image = gaussian_blur(new_image)
new_image = calculate_gradient(new_image)

#gesture_x, gesture_y = int(input('Enter gesture coordinates: '))
#image_with_selected_obj = select_obj(image, gesture_x, gesture_y)
new_image.show()
