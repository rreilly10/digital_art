import numpy as np
from PIL import Image


def create_circular_mask(h, w, center=None, radius=None):

    if center is None:  # use the middle of the image
        center = (int(w / 2), int(h / 2))
    if radius is None:  # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w - center[0], h - center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0]) ** 2 + (Y - center[1]) ** 2)

    mask = dist_from_center <= radius
    return mask


if __name__ == "__main__":
    img1 = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/grass.jpeg"
    )
    img1 = np.asarray(img1)

    img2 = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/redwood.jpg"
    )
    img2 = np.asarray(img2)

    from digart.utils import utils

    img1, img2 = utils.align_images(img1, img2)

    h, w = img1.shape[:2]

    mask = create_circular_mask(h, w, center=(1, 1))

    # mask = create_circular_mask(h, w)

    # img1[~mask] = img1[~mask].mean(axis=(0, 1))
    # img1[~mask] = img2[~mask]
    img1[mask] = 0

    center = (int(w / 2), int(h / 2))
    mask = create_circular_mask(h, w, center=(100, 100))

    img1[mask] = 400

    Image.fromarray(img1).show()
