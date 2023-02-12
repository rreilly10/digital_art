import numpy as np
from PIL import Image

from pipeline.transforms.image_transform import ImageTransform


class SpliceVerticallyTransform(ImageTransform):
    def apply(self, image, target_image, step_size: int = 1) -> np.array:
        # convert images to numpy arrays
        image = np.asarray(image)
        target_image = np.asarray(target_image)

        # raise an exception if the images are not the same size
        if image.shape != target_image.shape:
            raise Exception(
                f"img1: {image.shape} img2: {target_image.shape} do not match - unable to splice images"
            )

        switch = True
        for i in range(0, len(image[0]), step_size):
            if switch:
                image[::, i : i + step_size] = target_image[::, i : i + step_size]
            switch = not switch

        return Image.fromarray(image)


if __name__ == "__main__":
    splice_vertically = SpliceVerticallyTransform()

    image = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/bkly_bridge.jpg"
    )
    image2 = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/dumbo.jpg"
    )

    out = splice_vertically.apply(image=image, target_image=image2, step_size=20)

    out.show()
