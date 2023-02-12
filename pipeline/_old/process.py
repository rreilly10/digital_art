import os

from exif import Image
import random

from image_container import ImageContainer


def load_images(path):
    images = []
    for filename in os.listdir(path):
        f = os.path.join(path, filename)

        # checking if it is .jpg
        if os.path.isfile(f) and ".jpg" in f or ".jpeg" in f:
            images.append(
                ImageContainer(
                    image_path=f,
                    cache_path="/Users/robertreilly/code/digital_art/assets/images/out/large_comp",
                )
            )

    return images


def create_grid(images):
    grid = []
    i = 0

    random.shuffle(images)

    for img in images:
        for img2 in images[::-1]:
            print(f"{i} images processed")
            if img == img2:
                continue

            spliced = img.splice_alternate(
                img2,
            )
            # spliced.show_image()
            spliced.save(
                folder_path="/Users/robertreilly/code/digital_art/assets/images/out/large_comp"
            )

            i += 1


if __name__ == "__main__":
    try:
        os.environ["PYTHONHASHSEED"]
    except Exception as exception:
        print(exception)
        print(f"Set PYTHONHASHSEED with `export PYTHONHASHSEED=0`")
        exit

    images = load_images(
        "/Users/robertreilly/code/digital_art/assets/images/src_to_process"
    )
    grid = create_grid(images=images)
