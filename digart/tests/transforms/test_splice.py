from digart.transforms.splice import (
    splice_alternate,
    splice_vertically,
    splice_horizontally,
)

import numpy as np


def test_splice_alternate_on_same_sized_images():
    img1 = np.asarray(
        [
            [[0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0]],
        ],
        dtype=np.uint8,
    )

    img2 = np.asarray(
        [
            [[255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )

    spliced = splice_alternate(img1=img1, img2=img2)

    expected = np.asarray(
        [
            [[255, 255, 255], [0, 0, 0]],
            [[0, 0, 0], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )
    assert np.array_equal(spliced, expected)


def test_splice_vertically_on_same_sized_images():
    img1 = np.asarray(
        [
            [[0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0]],
        ],
        dtype=np.uint8,
    )

    img2 = np.asarray(
        [
            [[255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )

    spliced = splice_vertically(img1=img1, img2=img2)

    expected = np.asarray(
        [
            [[255, 255, 255], [0, 0, 0]],
            [[255, 255, 255], [0, 0, 0]],
        ],
        dtype=np.uint8,
    )
    assert np.array_equal(spliced, expected)


def test_splice_horizontally_on_same_sized_images():
    img1 = np.asarray(
        [
            [[0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0]],
        ],
        dtype=np.uint8,
    )

    img2 = np.asarray(
        [
            [[255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255]],
        ],
        dtype=np.uint8,
    )

    spliced = splice_horizontally(img1=img1, img2=img2)

    expected = np.asarray(
        [
            [[255, 255, 255], [255, 255, 255]],
            [[0, 0, 0], [0, 0, 0]],
        ],
        dtype=np.uint8,
    )
    assert np.array_equal(spliced, expected)
