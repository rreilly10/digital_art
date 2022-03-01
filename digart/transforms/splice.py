import math
import os
from datetime import datetime
from digart.utils.utils import get_image_name_from_path
import numpy as np
from PIL import Image

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

    for i in range(0, len(img1), square):
        for j in range(0, len(img1[i]), square):
            if (i + j) % 2 == 0:
                # fmt: off
                img1[i : i + square, j : j + square] = img2[i : i + square, j : j + square]
    return img1

def align_images(img1, img2):
    h = min(img1.shape[0], img2.shape[0])
    w = min(img1.shape[1], img2.shape[1])

    if img1.shape[0] != h:
        padding = (img1.shape[0] - h) / 2 
        img1 = img1[math.floor(padding): img1.shape[0]-math.ceil(padding)]

    if img2.shape[0] != h:
        padding = (img2.shape[0] - h) / 2 
        img2 = img2[math.floor(padding): img2.shape[0]-math.ceil(padding)]

    if img1.shape[1] != w:
        padding = (img1.shape[1] - w) / 2 
        img1 = img1[:, math.floor(padding): img1.shape[1]-math.ceil(padding)]

    if img2.shape[1] != w:
        padding = (img2.shape[1] - w) / 2 
        img2 = img2[:, math.floor(padding): img2.shape[1]-math.ceil(padding)]

    if img1.shape != img2.shape:
        raise Exception(f'{img1.shape} does not equal {img2.shape}')
    
    return img1, img2


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


# spliced = pixelate(
#     img1, square=15, alternate=True
# )


def grid_search(dir):
    os.chdir(dir)
    files = os.listdir(dir)
    combs = set()
    for i, src in enumerate(files):
        for dst in files[i:]:
            pairs = os.path.abspath(src), os.path.abspath(dst)
            combs.add(pairs)
    os.chdir('..')
    return combs


def process_images(img1_path, img2_path, functions=[]):
    img1, img2 = align_images(np.asarray(Image.open(img1_path)), np.asarray(Image.open(img2_path)))
    
    for func in functions:
        img1 = func(img1, img2, 1)
    
    img = Image.fromarray(img1)
    os.makedirs(f'out/{now.strftime("%d-%m-%Y")}/{get_image_name_from_path(img1_path)}', exist_ok = True) 
    
    img.save(f'out/{now.strftime("%d-%m-%Y")}/{get_image_name_from_path(img1_path)}/{get_image_name_from_path(img2_path)}.jpg', "JPEG")
    # img.show()


