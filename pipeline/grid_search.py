import hashlib
from PIL import Image
from pipeline.transforms import *
from pipeline.image_wrapper import ImageWrapper
from pipeline.image_transformations import ImageTransformations
from collections import defaultdict
from itertools import product


def perform_grid_search(images, transforms, depth=1, cache={}):
    results = []

    images = [ImageWrapper(i) for i in images]

    transform_dict = defaultdict(list)

    for transform in transforms:
        transform_class = transform[0]
        for transform_variant_type, variants in transform[1].items():
            for variant in variants:
                # tmp_transformer = ImageTransformations()

                # tmp_transformer.add_transform(
                #     transform_class, **{transform_variant_type: variant}
                # )

                transform_dict[transform_class.__class__.__name__].append(
                    (transform_class, variant)
                )

    transform_grid = list(
        product(transform_dict["RotateTransform"], transform_dict["FlipTransform"])
    )
    transform_grid = list(product(*transform_dict.values()))

    return transform_grid


if __name__ == "__main__":
    image = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/c_park.jpg"
    )
    image2 = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/redwood.jpg"
    )

    images = [image, image2]

    rotate_transform = RotateTransform()
    # transformer.add_transform(rotate_transform, angle=45)

    flip_transform = FlipTransform()
    # transformer.add_transform(flip_transform, axis="horizontal")

    pixelate_transform = PixelateTransform()
    # transformer.add_transform(pixelate_transform, square_size=25)

    transforms = [
        [RotateTransform(), {"angle": [45, 90, 180]}],
        [FlipTransform(), {"axis": ["horizontal"]}],
        [PixelateTransform(), {"square_size": [20, 50, 100]}],
    ]

    transform_grid = perform_grid_search(images, transforms)

    tmp_transform = ImageTransformations()
    for t in transform_grid[6]:
        tmp_transform.add_transform(*t)

    print(tmp_transform.transforms)

    i = ImageWrapper(image=image, image_transforms=tmp_transform)
    print(i.image_transforms.transforms)
    i.show()
