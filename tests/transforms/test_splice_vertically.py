from pipeline.transforms.splice_vertically import SpliceVerticallyTransform
import numpy as np

import pytest


@pytest.fixture
def splice_vertically_transform():
    return SpliceVerticallyTransform()


def test_splice_vertically_on_same_sized_images(splice_vertically_transform):
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

    spliced = splice_vertically_transform.apply(
        image=img1, target_image=img2, step_size=1
    )

    expected = np.asarray(
        [
            [[255, 255, 255], [0, 0, 0]],
            [[255, 255, 255], [0, 0, 0]],
        ],
        dtype=np.uint8,
    )
    assert np.array_equal(spliced, expected)


# def test_splice_horizontally_on_same_sized_images():
#     img1 = np.asarray(
#         [
#             [[0, 0, 0], [0, 0, 0]],
#             [[0, 0, 0], [0, 0, 0]],
#         ],
#         dtype=np.uint8,
#     )

#     img2 = np.asarray(
#         [
#             [[255, 255, 255], [255, 255, 255]],
#             [[255, 255, 255], [255, 255, 255]],
#         ],
#         dtype=np.uint8,
#     )

#     spliced = splice_horizontally(img1=img1, img2=img2)

#     expected = np.asarray(
#         [
#             [[255, 255, 255], [255, 255, 255]],
#             [[0, 0, 0], [0, 0, 0]],
#         ],
#         dtype=np.uint8,
#     )
#     assert np.array_equal(spliced, expected)
