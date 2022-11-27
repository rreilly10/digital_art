from ctypes import util
import numpy as np
import random
import copy

from pytest import ExceptionInfo

from digart.utils import utils

def get_random_sample(randoms):
    return randoms[random.randint(0, len(randoms) - 1)]


def random_sample_n_images(images, square=1, seed=None):
    if seed:
        random.seed(seed)

    num_squares = int((images[0].shape[0] * images[0].shape[1]) / square)
    randoms = []

    for _ in range(num_squares):
        randoms.append(random.randint(0, len(images) - 1))

    for i in range(0, len(images[0]), square):
        for j in range(0, len(images[0][i]), square):
            # fmt: off
            images[0][i : i + square, j : j + square] = images[get_random_sample(randoms)][i : i + square, j : j + square]
    return images[0]


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

    # pixed = random_sample_n_images(
    #     images=[
    #         copy.deepcopy(img1),
    #         copy.deepcopy(img2),
    #         copy.deepcopy(img2),
    #         copy.deepcopy(img2),
    #         copy.deepcopy(img1),
    #     ],
    #     square=1,
    #     seed=None,
    # )

    from PIL import Image
    import copy

    import os

    images = []
    
    path = "/Users/robertreilly/code/digital_art/assets/videos/backflip/frames"
    path = "/Users/robertreilly/code/digital_art/assets/videos/ppl/frames"
    
    path = "/Users/robertreilly/code/digital_art/assets/images/src"
    path = "/Users/robertreilly/code/digital_art/assets/images/out/01-03-2022/celest.jpg"

    print(os.listdir(path))
    
    mx = None
    my = None
    
    for image in os.listdir(path):
        try:
            img = np.asarray(Image.open(f"{path}/{image}"))
            
            if isinstance(mx, type(None)) or img.shape[0] < mx.shape[0]:
                mx = img
            
            if isinstance(my, type(None)) or img.shape[1] < my.shape[1]:
                my = img
            
            images.append(img)
        except Exception as exception:
            print(exception)

    print(mx.shape)
    print(my.shape)
    
    for i in range(len(images)):
        images[i], _ = utils.align_images(images[i], mx)
        images[i], _ = utils.align_images(images[i], my)

    print(set([i.shape for i in images]))


    pixed = random_sample_n_images(images=images, square=1, seed=None)

    Image.fromarray(pixed).show()
