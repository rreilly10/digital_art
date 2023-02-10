import shutil
import os

LOCAL_LIKE = "/Users/robertreilly/code/digital_art/assets/images/out/like"
LOCAL_DISLIKE = "/Users/robertreilly/code/digital_art/assets/images/out/dislike"


def move_file_locally(src_path, dst_path):
    shutil.move(src_path, dst_path)


def like_local(image_path):
    image_name = os.path.basename(image_path)

    move_file_locally(image_path, f"{LOCAL_LIKE}/{image_name}")


def dislike_local(image_path):
    image_name = os.path.basename(image_path)

    move_file_locally(image_path, f"{LOCAL_DISLIKE}/{image_name}")
