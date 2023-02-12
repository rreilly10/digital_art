from PIL import Image
from transforms.flip import FlipTransform
from transforms.resize import ResizeTransform
from transforms.rotate import RotateTransform
from transforms.pixelate import PixelateTransform

from pipeline.image_transformations import ImageTransformations

from pipeline.image_wrapper import ImageWrapper


if __name__ == "__main__":
    image = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/c_park.jpg"
    )

    transformer = ImageTransformations()

    rotate_transform = RotateTransform()
    transformer.add_transform(rotate_transform, angle=45)

    flip_transform = FlipTransform()
    transformer.add_transform(flip_transform, axis="horizontal")

    img_wrapper = ImageWrapper(image=image, image_transforms=transformer, metadata={})

    pixelate_transform = PixelateTransform()
    # transformer.add_transform(pixelate_transform, square_size=25)

    img_wrapper.add_transform(pixelate_transform, square_size=25)

    # print(img_wrapper.get_hash())
    # img_wrapper.show()

    img_wrapper.show()
    print(img_wrapper.peek_next_transform_hash(pixelate_transform, square_size=5))
    img_wrapper.show()
