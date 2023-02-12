import numpy as np
from PIL import Image

from pipeline.transforms.image_transform import ImageTransform


class SpliceAlternatingTransform(ImageTransform):
    def apply(self, image, target_image, square_size: int = 1) -> np.array:
        # convert images to numpy arrays
        image = np.asarray(image)
        target_image = np.asarray(target_image)

        # raise an exception if the images are not the same size
        if image.shape != target_image.shape:
            raise Exception(
                f"img1: {image.shape} img2: {target_image.shape} do not match - unable to splice images"
            )

        for i in range(0, len(image), square_size):
            for j in range(0, len(image[i]), square_size):
                if (i + j) % 2 == 0:
                    # fmt: off
                    image[i : i + square_size, j : j + square_size] = \
                        target_image[i : i + square_size, j : j + square_size]
                    # fmt: on
        return Image.fromarray(image)
