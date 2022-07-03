def pixelate(img1, square=1, alternate=False):
    switch = True
    for i in range(0, len(img1), square):
        for j in range(0, len(img1[i]), square):
            if switch:
                # fmt: off
                img1[i : i + square, j : j + square] = img1[i : i + square, j : j + square].mean(axis=(0, 1))
            if alternate:
                switch = not switch
    return img1


