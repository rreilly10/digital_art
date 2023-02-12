import numpy as np

from pipeline.utils.utils import align_images


def test_align_identical_images():
    """expect both images to be unchanged"""

    # fmt: off
    img1 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    img2 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    # fmt: on

    img1, img2 = align_images(img1=img1, img2=img2)

    assert np.array_equal(img1, img2)
    assert np.array_equal(img2, img1)


def test_align_two_images_where_one_is_larger_by_1_to_the_right():
    """expect the larger to have its right element removed"""

    # fmt: off
    img1 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]],
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    img2 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    # fmt: on

    img1, img2 = align_images(img1=img1, img2=img2)

    assert np.array_equal(img1, img2)
    assert np.array_equal(img2, img1)

    img1, img2 = align_images(img1=img2, img2=img1)

    assert np.array_equal(img1, img2)
    assert np.array_equal(img2, img1)


def test_align_two_images_where_one_is_larger_by_1_to_the_right_and_left():
    """expect the larger image to be centered based on the smaller image dimensions"""

    # center example
    # fmt: off
    img1 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]],
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    img2 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    # fmt: on

    img1, img2 = align_images(img1=img1, img2=img2)

    assert np.array_equal(img1, img2)
    assert np.array_equal(img2, img1)

    img1, img2 = align_images(img1=img2, img2=img1)

    assert np.array_equal(img1, img2)
    assert np.array_equal(img2, img1)


def test_align_two_images_where_one_is_larger_on_both_sides():
    """expect the larger to just be the center two rows"""

    # center example
    # fmt: off
    img1 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]], # Sample the middle two rows
            [[7, 8, 9], [10, 11, 12]], # Sample the middle two rows
            [[7, 8, 9], [10, 11, 12]],
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    img2 = np.asarray(
        [
            [[1, 2, 3], [ 4,  5,  6]], 
            [[7, 8, 9], [10, 11, 12]]
        ], 
        np.uint8
    )
    # fmt: on

    img1, img2 = align_images(img1=img1, img2=img2)

    assert np.array_equal(
        img1,
        np.asarray([[[7, 8, 9], [10, 11, 12]], [[7, 8, 9], [10, 11, 12]]], np.uint8),
    )
    assert np.array_equal(
        img2, np.asarray([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], np.uint8)
    )


def test_align_real_images():
    from PIL import Image

    img1 = Image.open(
        "/Users/robertreilly/code/digital_art/assets/images/src/greece.jpg"
    )
    img1 = np.asarray(img1)

    img2 = Image.open("/Users/robertreilly/code/digital_art/assets/images/src/bean.jpg")
    img2 = np.asarray(img2)

    img1, img2 = align_images(img1=img2, img2=img1)

    print(img1.shape, img2.shape)
