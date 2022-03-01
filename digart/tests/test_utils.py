from digart.utils.utils import get_image_name_from_path
from pytest import fixture


@fixture
def test_path():
    return "/test/path/name.jpeg"


def test_get_image_name_from_path_default(test_path):
    assert get_image_name_from_path(test_path) == "name.jpeg"


def test_get_image_name_from_path_no_extension(test_path):
    assert get_image_name_from_path(test_path, extension=False) == "name"
