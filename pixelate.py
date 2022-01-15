import numpy as np
import plotly.express as px
from PIL import Image

file = "/Users/rr/Desktop/code/digital_art/images/IMG_2871.jpeg"

color_img = np.asarray(Image.open(file))

image = Image.open(file)


data = np.asarray(image)
data = np.rot90(data, 3)


def pixelate(img, window):
    sign = 1
    n, m, _ = img.shape
    n = n - n % window
    m = m - m % window

    for x in range(0, n, window):
        for y in range(0, m, window):
            img[x : x + window, y : y + window] = img[
                x : x + window, y : y + window
            ].mean(axis=(0, 1))

        if window < 75 or window < 0:
            sign *= -1

        if window > 50:
            window += 3 * sign
        else:
            window -= 50 * sign

    return img


# n, m, _ = data.shape
# step = 1
# for x in range(0, n, step):
#     for y in range(0, m, step):
#         new_image = pixelate(data[x : x + step][y : y + step], step)
#         step += 1

new_image = pixelate(data, 50)
new_image = pixelate(data, 75)
new_image = Image.fromarray(new_image)
new_image.show()
