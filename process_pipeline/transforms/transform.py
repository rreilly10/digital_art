from abc import ABC, abstractmethod
from PIL import Image
import numpy as np


class Transform(ABC):
    def __init__(self, images: list):
        self.images = [self.img_from_path(i) for i in images]
        self.transformed_image = self.apply()

    @abstractmethod
    def apply(self):
        pass

    def img_from_path(self, path: str):
        img = Image.open(path)
        return np.asarray(img)

    def show(self):
        Image.fromarray(self.transformed_image).show()

    def save(path=None):
        pass


class SpliceAlternate(Transform):
    def apply(self):
        img1 = self.images[0]
        img2 = self.images[1]

        square = 4

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

        Image.fromarray(img1).show()

        self.transformed_image = img1
        return img1


t = SpliceAlternate(
    images=[
        "/Users/robertreilly/code/digital_art/assets/images/src/greece.jpg",
        "/Users/robertreilly/code/digital_art/assets/images/src/bkly_bridge.jpg",
    ]
)

t.show()
