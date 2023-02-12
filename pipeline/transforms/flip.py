from PIL import Image
from pipeline.transforms.image_transform import ImageTransform


class FlipTransform(ImageTransform):
    def apply(self, image, axis="horizontal"):
        if axis == "horizontal":
            return image.transpose(Image.FLIP_LEFT_RIGHT)
        elif axis == "vertical":
            return image.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Invalid axis")
