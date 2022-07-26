import math
import os
from pathlib import Path
from typing import Tuple

import cv2
import numpy as np


def align_images(img1: np.ndarray, img2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """This function attempts to align two images by taking the dimensions of the smaller image,
    and sampling the center of the larger image with those dimensions

    Args:
        img1 (np.ndarray)
        np (np.ndarray)

    Raises:
        Exception: assertion error if the output images do not have the same dimensions

    Returns:
        Tuple[np.ndarray, np.ndarray]: aligned images in a Tuple
    """

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


if __name__ == "__main__":
    img1 = np.asarray([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
    img2 = np.asarray([[[1, 2, 3], [4, 5, 6]]])

    # center example
    img1 = np.asarray(
        [
            [
                [10, 11, 12],
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        ]
    )
    img2 = np.asarray([[[1, 2, 3], [4, 5, 6]]])

    img1, img2 = align_images(img1=img1, img2=img2)

    print(img1)
    print(img2)

    assert np.array_equal(img1, img2)
    assert np.array_equal(img2, img1)


def video_to_frames(video_path, name=None):
    name = name or os.path.basename(video_path)
    path = Path(video_path).parent

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    if not os.path.isdir(f"{path}/frames"):
        os.makedirs(f"{path}/frames")

    while success:
        print(f'writing to {path}/frames/frame_{count}.jpg"')
        cv2.imwrite(f"{path}/frames/frame_{count}.jpg", image)

        success, image = vidcap.read()
        print("Read a new frame: ", success)
        count += 1


if __name__ == "__main__":
    video_to_frames(
        "/Users/robertreilly/code/digital_art/assets/videos/ppl/ppl_zoom_out.MOV"
    )
