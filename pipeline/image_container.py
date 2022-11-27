import hashlib
import os
from os.path import exists

import numpy as np
from digart.transforms.splice import splice_alternate
from digart.utils.utils import align_images
from PIL import Image
from PIL.ExifTags import TAGS


class ImageContainer:
    def __init__(
        self,
        image_path: str = None,
        image: np.array = None,
        prior_transforms: list = [],
        cache_path: str = None,
    ):
        self.image_path = image_path
        self.cache_path = cache_path

        if self.image_path:
            self.image_name = os.path.basename(self.image_path)

        if image is not None:
            self.image = image
        else:
            self.image = self._load_image()

        self.prior_transforms = prior_transforms

    def show_image(self):
        Image.fromarray(self.image).show()

    def splice_alternate(self, target_image, square=1):
        if self.cache_path:
            prior_transforms = {
                "transform": "splice_alternate",
                "img1": self.image_name,
                "img2": target_image.image_name,
                "square": square,
            }
            check_hash = hash(f"None-{str(prior_transforms)}")

            img_cache_path = f"{self.cache_path}/{check_hash}.jpg"
            if exists(img_cache_path):
                print(f"{img_cache_path} already exists using cache")
                return ImageContainer(
                    image=np.asarray(Image.open(img_cache_path)),
                    prior_transforms={
                        "transform": "splice_alternate",
                        "img1": self.image_name,
                        "img2": target_image.image_name,
                        "square": square,
                    },
                )

        target_image_np = np.asarray(Image.open(target_image.image_path))

        img1, img2 = align_images(self.image, target_image_np)

        spliced = splice_alternate(img1=img1, img2=img2, square=square)

        return ImageContainer(
            image=spliced,
            prior_transforms={
                "transform": "splice_alternate",
                "img1": self.image_name,
                "img2": target_image.image_name,
                "square": square,
            },
        )

    def save(self, folder_path):
        Image.fromarray(self.image).save(f"{folder_path}/{self.__hash__()}.jpg")

    def __eq__(self, other):
        return (
            self.image_path == other.image_path
            and self.prior_transforms == other.prior_transforms
        )

    def __key_combination(self):
        return f"{self.image_name}-{self.prior_transforms}"

    def __hash__(self) -> int:
        return hash(self.__key_combination())

    def _load_image_metadata(self):
        img = Image.open(self.image_path)

        metadata = {
            "file_path": img.filename,
            "file_name": self.image_name,
            "image_size": img.size,
            "image_height": img.height,
            "image_width": img.width,
            "image_format": img.format,
            "image_mode": img.mode,
            "animated": getattr(img, "is_animated", False),
            "frames": getattr(img, "n_frames", 1),
        }

        exifdata = img.getexif()
        for tag_id in img.getexif():

            data = exifdata.get(tag_id)
            tag = TAGS.get(tag_id)

            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            metadata[tag] = data

        return metadata

    def _load_image(self):
        self.image = np.asarray(Image.open(self.image_path))
        return self.image

    def __getattr__(self, __name: str):
        if __name == "metadata":
            self.metadata = self._load_image_metadata()
            return self.metadata


def get_image_metadata(image_path):

    img = Image.open(image_path)

    metadata = {
        "Filename": img.filename,
        "Image Size": img.size,
        "Image Height": img.height,
        "Image Width": img.width,
        "Image Format": img.format,
        "Image Mode": img.mode,
        "Image is Animated": getattr(img, "is_animated", False),
        "Frames in Image": getattr(img, "n_frames", 1),
    }

    exifdata = img.getexif()
    for tag_id in img.getexif():
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
            metadata[tag] = data

    return metadata


if __name__ == "__main__":
    ic = ImageContainer(
        image_path="/Users/robertreilly/code/digital_art/assets/images/src_to_process/IMG_9339.JPG",
    )

    other = ImageContainer(
        image_path="/Users/robertreilly/code/digital_art/assets/images/src_to_process/IMG_8012.JPG"
    )
    new = ic.splice_alternate(other)

    new.show_image()
