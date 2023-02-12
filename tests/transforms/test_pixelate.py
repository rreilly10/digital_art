import numpy as np
import pytest

from pipeline.transforms.pixelate import PixelateTransform


@pytest.fixture
def pixelate_transform():
    return PixelateTransform()


def test_pixelate_with_square_2(pixelate_transform):
    img = np.asarray(
        [
            [[1, 1, 1], [255, 255, 255]],
            [[255, 255, 255], [1, 1, 1]],
        ],
        dtype=np.uint8,
    )

    out = pixelate_transform.apply(img, square_size=2)

    expected = np.asarray(
        [
            [[128, 128, 128], [128, 128, 128]],
            [[128, 128, 128], [128, 128, 128]],
        ],
        dtype=np.uint8,
    )

    assert np.array_equal(out, expected)
