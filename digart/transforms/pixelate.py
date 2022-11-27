import numpy as np

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


if __name__ == "__main__":
    img1 = np.asarray(
        [
            [[1, 1, 1], [1, 1, 1], [255, 255, 255], [255, 255, 255]],
            [[255, 255, 255], [255, 255, 255], [1, 1, 1], [1, 1, 1],],
        ],
        dtype=np.uint8,
    )

    from PIL import Image
    
    
    Image.fromarray(img1).show()
    pixed = pixelate(img1, square=2, alternate=True)

    print(pixed)


    Image.fromarray(pixed).show()
