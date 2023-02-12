import hashlib
import pickle


class ImageTransformations:
    def __init__(self):
        self.transforms = []

    def add_transform(self, transform, *args, **kwargs):
        self.transforms.append((transform, args, kwargs))

    def clear_transforms(self):
        self.transforms = []

    def get_transforms(self):
        return self.transforms

    # def get_transformed_hash(self, image):
    #     for transform in self.transforms:
    #         transform_function = transform[0]
    #         args = transform[1]
    #         kwargs = transform[2]
    #         hash_input = transform_function.apply(image, *args, **kwargs)
    #     serialized = pickle.dumps((hash_input, self.transforms, image.filename))
    #     return hashlib.sha256(serialized).hexdigest()

    # def peek_next_transform_hash(self, image, transform, *args, **kwargs):
    #     pass

    def apply_transforms(self, image):
        for transform, args, kwargs in self.transforms:
            image = transform.apply(image, *args, **kwargs)
        return image


if __name__ == "__main__":
    # transform usage examples

    from PIL import Image

    from pipeline.transforms import *

    image = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/c_park.jpg"
    )

    # define transform objects
    flip = FlipTransform()
    rotate = RotateTransform()

    # define transformer
    transformer = ImageTransformations()

    # add transforms to transformer
    transformer.add_transform(flip, axis="horizontal")
    transformer.add_transform(rotate, angle=20)

    # apply the transformer to an image
    image = transformer.apply_transforms(image)

    # show the image
    # image.show()

    # Splice example

    splice = SpliceAlternatingTransform()

    image = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/bkly_bridge.jpg"
    )
    image2 = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/dumbo.jpg"
    )

    transformer = ImageTransformations()

    transformer.add_transform(splice, target_image=image2, square_size=1)

    img = transformer.apply_transforms(image=image)
    img.show()
