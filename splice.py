import numpy as np
import plotly.express as px
from PIL import Image


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


img1_path = "/Users/rr/Desktop/code/digital_art/images/bkly_bridge.jpg"
img2_path = "/Users/rr/Desktop/code/digital_art/images/dumbo.jpg"


spliced = splice_images_vertically(
    img1=np.asarray(Image.open(img1_path)),
    img2=np.asarray(Image.open(img2_path)),
    step=2,
)
# spliced = splice_images_horizontally(
#     img1=spliced,
#     img2=np.asarray(Image.open(img2_path)),
#     step=1,
# )

Image.fromarray(spliced).show()
