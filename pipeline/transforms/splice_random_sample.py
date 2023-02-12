import random

import numpy as np
from PIL import Image

from pipeline.transforms.image_transform import ImageTransform


class SpliceRandomSampleTransform(ImageTransform):
    def apply(self, image, target_image, square_size: int = 1, seed=None) -> np.array:
        # convert images to numpy arrays
        image = np.asarray(image)
        target_image = np.asarray(target_image)

        # raise an exception if the images are not the same size
        if image.shape != target_image.shape:
            raise Exception(
                f"img1: {image.shape} img2: {target_image.shape} do not match - unable to splice images"
            )

        if seed:
            random.seed(seed)

        num_squares = int((image.shape[0] * image.shape[1]) / square_size)
        randoms = []

        for _ in range(num_squares):
            randoms.append(random.random())

        for i in range(0, len(image), square_size):
            for j in range(0, len(image[i]), square_size):
                # if randoms[i+j] > .5: # diagonal
                if self.get_random_sample(randoms) > 0.5:
                    # fmt: off
                    image[i : i + square_size, j : j + square_size] = \
                        target_image[i : i + square_size, j : j + square_size]
                    # fmt: on
        return Image.fromarray(image)

    def get_random_sample(self, randoms):
        return randoms[random.randint(0, len(randoms) - 1)]


if __name__ == "__main__":
    splice_random = SpliceRandomSampleTransform()

    image = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/bkly_bridge.jpg"
    )
    image2 = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/dumbo.jpg"
    )

    out = splice_random.apply(image=image, target_image=image2, square_size=5)

    out.show()
