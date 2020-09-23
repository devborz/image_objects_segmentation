from PIL import Image, ImageDraw


def set_monotone(image: Image):
    draw = ImageDraw.Draw(image)
    pix = image.load()
    width = image.size[0]
    height = image.size[1]
    for x in range(width):
        for y in range(height):
            r = int(0.299*pix[x, y][0] + 0.587*pix[x, y][1]
                + 0.114*pix[x, y][2])
            g = int(0.299*pix[x, y][0] + 0.587*pix[x, y][1]
                + 0.114*pix[x, y][2])
            b = int(0.299*pix[x, y][0] + 0.587*pix[x, y][1]
                + 0.114*pix[x, y][2])
            draw.point((x, y), (r, g, b))

    image.save("/Users/usman/Desktop/result.jpg", "JPEG")
    return image


def select_obj(image: Image, gesture_x: int, gesture_y: int):
    return image


path = '/Users/usman/Desktop/' + input('Enter image path: ')
image: Image = Image.open(path)
set_monotone(image)

# gesture_x, gesture_y = int(input('Enter gesture coordinates: '))
# image_with_selected_obj = select_obj(image, gesture_x, gesture_y)
# image_with_selected_obj.show()
