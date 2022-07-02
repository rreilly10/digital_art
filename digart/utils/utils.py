import os
import numpy as np

from PIL import Image
import math


def get_image_name_from_path(img_path, extension=True):
    image_name = img_path.split("/")[-1]
    if extension:
        return image_name
    return image_name.split(".")[0]


def path_to_np_array(image_path):
    return np.asarray(Image.open(image_path))


def np_array_to_img(np_array):
    return Image.fromarray(np_array)


def grid_search(dir):
    os.chdir(dir)
    files = os.listdir(dir)
    combs = set()
    for i, src in enumerate(files):
        for dst in files[i:]:
            if src != dst:
                pairs = os.path.abspath(src), os.path.abspath(dst)
                combs.add(pairs)
    os.chdir("..")
    return combs


def align_images(img1, img2):
    h = min(img1.shape[0], img2.shape[0])
    w = min(img1.shape[1], img2.shape[1])

    if img1.shape[0] != h:
        padding = (img1.shape[0] - h) / 2
        img1 = img1[math.floor(padding) : img1.shape[0] - math.ceil(padding)]

    if img2.shape[0] != h:
        padding = (img2.shape[0] - h) / 2
        img2 = img2[math.floor(padding) : img2.shape[0] - math.ceil(padding)]

    if img1.shape[1] != w:
        padding = (img1.shape[1] - w) / 2
        img1 = img1[:, math.floor(padding) : img1.shape[1] - math.ceil(padding)]

    if img2.shape[1] != w:
        padding = (img2.shape[1] - w) / 2
        img2 = img2[:, math.floor(padding) : img2.shape[1] - math.ceil(padding)]

    if img1.shape != img2.shape:
        raise Exception(f"{img1.shape} does not equal {img2.shape}")

    return img1, img2
