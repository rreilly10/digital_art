import hashlib
import pickle

from PIL import Image

from pipeline.image_transformations import ImageTransformations
import copy


class ImageWrapper:
    def __init__(
        self,
        image: Image,
        image_transforms: ImageTransformations = None,
        metadata: dict = {},
    ):
        self.image = image
        if image_transforms is None:
            image_transforms = ImageTransformations()

        # Copying so that additions to the passed transform from outside
        # of this class do not result in updates to this image.
        # We want to fully control transforms to this image from this
        # image explicitly.
        self.image_transforms = copy.deepcopy(image_transforms)
        self.metadata = metadata

    def add_transform(self, transform, *args, **kwargs):
        self.image_transforms.add_transform(transform, *args, **kwargs)

        # TODO - think about if we should apply here or not
        # considering future lazy load case to derive hash before we
        # actually go through the trouble of creating the image

        # self.image = self.image_transforms.apply_transforms(self.image)

    def get_hash(self, additional_transforms=None):
        hash_input = ""

        transforms = self.image_transforms.transforms

        if additional_transforms:
            transforms = additional_transforms.transforms

        for transform in transforms:
            transform_function = transform[0]
            args = transform[1]
            kwargs = transform[2]
            hash_input = transform_function.apply(image=self.image, *args, **kwargs)

        # The fact that this shows an untransformed image proves
        # that we are correctly lazy loading the image and
        # not pre-generating it before it is asked for.
        # This is great for future cache optomization on this hash
        # self.image.show()

        serialized = pickle.dumps((hash_input, transforms, self.image.filename))
        return hashlib.sha256(serialized).hexdigest()

    def peek_next_transform_hash(self, transform, *args, **kwargs):
        tmp_transformer = copy.deepcopy(self.image_transforms)
        tmp_transformer.add_transform(transform, *args, **kwargs)
        return self.get_hash(additional_transforms=tmp_transformer)

    def __eq__(self, other):
        return self.get_hash() == other.get_hash()

    def get_transformed_image(self):
        return self.image_transforms.apply_transforms(self.image)

    def show(self):
        self.get_transformed_image().show()
