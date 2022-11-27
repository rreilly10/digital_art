import numpy as np
import random

def get_random_sample(randoms):
    return randoms[random.randint(0, len(randoms)-1)]



def random_sample_two_images(img1, img2, square=1, seed=None):
    if img1.shape != img2.shape:
        raise Exception(
            f"img1: {img1.shape} img2: {img2.shape} do not match - unable to splice images"
        )

    if seed:
        random.seed(seed)

    num_squares = int((img1.shape[0] * img1.shape[1]) / square)
    randoms = []

    for _ in range(num_squares):
        randoms.append(random.random())

    for i in range(0, len(img1), square):
        for j in range(0, len(img1[i]), square):
            # if randoms[i+j] > .5: # diagonal
            if get_random_sample(randoms) > .5:
                # fmt: off
                img1[i : i + square, j : j + square] = img2[i : i + square, j : j + square]
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

    from PIL import Image
    import copy
    
    img1 = Image.open('/Users/robertreilly/code/digital_art/assets/images/grass.jpeg')
    img1 = np.asarray(img1)

    img2 = Image.open('/Users/robertreilly/code/digital_art/assets/images/maples.jpeg')
    img2 = np.asarray(img2)

    from digart.utils import utils

    img1, img2 = utils.align_images(img1, img2)

    pixed = random_sample_two_images(img1=copy.deepcopy(img1), img2=copy.deepcopy(img2), square=1, seed=None) 
        
    Image.fromarray(pixed).show()
