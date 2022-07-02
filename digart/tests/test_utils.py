from digart.utils.utils import get_image_name_from_path
from pytest import fixture
import numpy as np


@fixture
def test_path():
    return "/test/path/name.jpeg"


# Test get_image_name_from_path


def test_get_image_name_from_path_default(test_path):
    assert get_image_name_from_path(test_path) == "name.jpeg"


def test_get_image_name_from_path_no_extension(test_path):
    assert get_image_name_from_path(test_path, extension=False) == "name"


def test_grid_search():
    pass


def test_generate_test_images():
    I = np.arange(5)
    matrix = np.column_stack((3 * I, I**2))
    print(matrix)


def test_align_images():
    pass
