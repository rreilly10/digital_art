def splice_alternate(img1, img2, square=1):
    if img1.shape != img2.shape:
        raise Exception(
            f"img1: {img1.shape} img2: {img2.shape} do not match - unable to splice images"
        )

    for i in range(0, len(img1), square):
        for j in range(0, len(img1[i]), square):
            if (i + j) % 2 == 0:
                # fmt: off
                img1[i : i + square, j : j + square] = img2[i : i + square, j : j + square]
    return img1

