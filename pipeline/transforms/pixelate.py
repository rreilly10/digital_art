import numpy as np
from PIL import Image
from pipeline.transforms.image_transform import ImageTransform


class PixelateTransform(ImageTransform):
    def apply(self, image, square_size=1):
        np_img = np.asarray(image)
       
        switch = True
        for i in range(0, len(np_img), square_size):
            for j in range(0, len(np_img[i]), square_size):
                if switch:
                    # fmt: off
                    np_img[i : i + square_size, j : j + square_size] = np_img[i : i + square_size, j : j + square_size].mean(axis=(0, 1))
        return Image.fromarray(np_img)


if __name__ == "__main__":
    img1 = np.asarray(
        [
            [[1, 1, 1], [1, 1, 1], [255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255], [1, 1, 1], [1, 1, 1],],
        ],
        dtype=np.uint8,
    )

    from PIL import Image
    

    

    image = Image.fromarray(img1)
    

    pixelate_transform = PixelateTransform()
    output = pixelate_transform.apply(image, square_size=10)

    output.show()
