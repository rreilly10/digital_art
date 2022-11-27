import copy

import numpy as np
from PIL import Image


def splice_alternate(img1: np.array, img2: np.array, square: int = 1) -> np.array:
    if img1.shape != img2.shape:
        raise Exception(
            f"img1: {img1.shape} img2: {img2.shape} do not match - unable to splice images"
        )

    for i in range(0, len(img1), square):
        for j in range(0, len(img1[i]), square):
            if (i + j) % 2 == 0:
                # fmt: off
                img1[i : i + square, j : j + square] = img2[i : i + square, j : j + square]
                # fmt: on
    return img1


def splice_vertically(img1, img2, step=1):
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


def splice_horizontally(img1, img2, step=1):
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


if __name__ == "__main__":
    img1 = np.asarray(
        [
            [[1, 1, 1], [1, 1, 1]],
            [[1, 1, 1], [1, 1, 1]],
        ],
        dtype=np.uint8,
    )

    img2 = np.asarray(
        [
            [[255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )

    spliced_alt = splice_alternate(img1=copy.deepcopy(img1), img2=copy.deepcopy(img2))
    spliced_vert = splice_vertically(img1=copy.deepcopy(img1), img2=copy.deepcopy(img2))

    Image.fromarray(spliced_alt).show()
    Image.fromarray(spliced_vert).show()
