def get_image_name_from_path(img_path, extension=True):
    image_name = img_path.split("/")[-1]
    if extension:
        return image_name
    return image_name.split(".")[0]
