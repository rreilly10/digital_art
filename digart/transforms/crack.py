from digart.utils.utils import (
    get_image_name_from_path,
    np_array_to_img,
    path_to_np_array,
    path_to_np_array,
)


from PIL import Image


def crack_image(path):
    np_image = path_to_np_array(image_path=path)

    mean = np_image.mean(axis=(0, 1))

    print(mean)
    for i in range(0, len(np_image)):
        for j in range(0, len(np_image[i])):
            if np_image[i][j].all() > mean.any():
                # if (
                #     np_image[i][j][0] > 100
                #     and np_image[i][j][1] > 100
                #     and np_image[i][j][2] > 100
                # ):
                np_image[i][j] = mean

    img = np_array_to_img(np_image)

    img.show()


if __name__ == "__main__":
    crack_image("/Users/robertreilly/code/digital_art/images/bkly_bridge.jpg")
