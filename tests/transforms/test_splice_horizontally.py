from pipeline.transforms.splice_horizontally import SpliceHorizontallyTransform
import numpy as np

import pytest


@pytest.fixture
def splice_horizontally_transform():
    return SpliceHorizontallyTransform()


def test_splice_horizontally_on_same_sized_images(splice_horizontally_transform):
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

    spliced = splice_horizontally_transform.apply(
        image=img1, target_image=img2, step_size=1
    )

    expected = np.asarray(
        [
            [[255, 255, 255], [255, 255, 255]],
            [[0, 0, 0], [0, 0, 0]],
        ],
        dtype=np.uint8,
    )
    assert np.array_equal(spliced, expected)
