import numpy as np
from pipeline.transforms.pixelate import pixelate


def test_pixelate_with_square_2():
    img = np.asarray(
        [
            [[1, 1, 1], [255, 255, 255]],
            [[255, 255, 255], [1, 1, 1]],
        ],
        dtype=np.uint8,
    )

    pixed = pixelate(img, square=2)

    expected = np.asarray(
        [
            [[128, 128, 128], [128, 128, 128]],
            [[128, 128, 128], [128, 128, 128]],
        ],
        dtype=np.uint8,
    )

    assert np.array_equal(pixed, expected)


def test_pixelate_with_square_2_and_alternate_set_to_true():
    # fmt: off
    img = np.asarray(
        [
            [[1, 1, 1], [1, 1, 1], [255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255], [1, 1, 1], [1, 1, 1]],
        ],
        dtype=np.uint8,
    )
    # fmt: on

    pixed = pixelate(img, square=2, alternate=True)

    expected = np.asarray(
        [
            [[128, 128, 128], [128, 128, 128], [255, 255, 255], [255, 255, 255]],
            [[128, 128, 128], [128, 128, 128], [1, 1, 1], [1, 1, 1]],
        ],
        dtype=np.uint8,
    )

    assert np.array_equal(pixed, expected)
