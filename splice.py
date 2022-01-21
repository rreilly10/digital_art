import numpy as np
import plotly.express as px
from PIL import Image
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

def splice_images_horizontally(img1, img2, step=2):
    if img1.shape != img2.shape:
        raise Exception(
            f"img1: {img1.shape} img2: {img2.shape} do not match - unable to splice images"
        )

    switch = True
    for i in range(0, len(img1), step):
        if switch:
            img1[i : i + step, ::] = img2[i : i + step, ::]
        switch = not switch

    return img1


def splice_images_vertically(img1, img2, step=2):
    if img1.shape != img2.shape:
        raise Exception(
            f"img1: {img1.shape} img2: {img2.shape} do not match - unable to splice images"
        )

    switch = True
    for i in range(0, len(img1[0]), step):
        if switch:
            img1[::, i : i + step] = img2[::, i : i + step]
        switch = not switch

    return img1


def pixelate(img1, square=1, alternate=False):
    switch = True
    for i in range(0, len(img1), square):
        for j in range(0, len(img1[i]), square):
            if switch:
                # fmt: off
                img1[i : i + square, j : j + square] = img1[i : i + square, j : j + square].mean(axis=(0, 1))
            if alternate:
                switch = not switch
    return img1


def splice_alternate(img1, img2, square=1):
    if img1.shape != img2.shape:
        raise Exception(
            f"img1: {img1.shape} img2: {img2.shape} do not match - unable to splice images"
        )

    switch = True
    for i in range(0, len(img1), square):
        for j in range(0, len(img1[i]), square):
            if switch:
                # fmt: off
                img1[i : i + square, j : j + square] = img2[i : i + square, j : j + square]
            switch = not switch    
        switch = not switch    
            
    
    return img1


img1_path = "/Users/rr/Desktop/code/digital_art/images/woods.jpg"
img2_path = "/Users/rr/Desktop/code/digital_art/images/dumbo.jpg"

# spliced = splice_images_vertically(
#     img1=np.asarray(Image.open(img1_path)),
#     img2=np.asarray(Image.open(img2_path)),
#     step=2,
# )
# spliced = splice_images_horizontally(
#     np.asarray(Image.open(img1_path)),
#     np.asarray(Image.open(img2_path)),
#     step=1,
# )

spliced = splice_alternate(
    np.asarray(Image.open(img1_path)), np.asarray(Image.open(img2_path)), 1
)

# spliced = pixelate(
#     np.asarray(Image.open(img1_path)), square=15, alternate=True
# )

img = Image.fromarray(spliced)
img.save(f'out/{now.strftime("%d-%m-%Y-%H:%M:%S")}.jpg', "JPEG")
img.show()
