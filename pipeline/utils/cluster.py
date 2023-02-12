from re import S
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import random

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, k_means
from sklearn.metrics import pairwise_distances_argmin_min, pairwise_distances

X, y = make_blobs(
    n_samples=150,
    n_features=2,
    centers=3,
    cluster_std=0.5,
    shuffle=True,
    random_state=0,
)


if __name__ == "__main__":
    img = np.asarray(
        Image.open("/Users/robertreilly/code/digital_art/assets/images/src/redwood.jpg")
    )

    start_shape = img.shape

    img = img.reshape(-1, 3)

    km = KMeans(
        n_clusters=3, init="random", n_init=10, max_iter=300, tol=1e-04, random_state=0
    )
    y_km = km.fit_predict(img)

    closest, _ = pairwise_distances_argmin_min(km.cluster_centers_, img)

    print(km.transform(img))

    print(closest)

    img = img.reshape(start_shape)

    # Image.fromarray(img).show()


def visual(img, clusters):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("red")
    ax.set_ylabel("green")
    ax.set_zlabel("blue")

    sample_pixels = []
    sample_clusters = []
    seen_idx = set()

    for _ in range(5000):
        r = random.randint(0, len(img))

        if r not in seen_idx:
            sample_pixels.append(img[r])
            sample_clusters.append(y_km[r])

        seen_idx.add(r)

    sample_pixels = np.array(sample_pixels)
    sample_clusters = np.array(sample_clusters)

    print(sample_pixels.shape)
    print(sample_clusters.shape)

    print(len(sample_clusters), len(sample_pixels))

    ax.scatter(
        km.cluster_centers_[:, 0],
        km.cluster_centers_[:, 1],
        km.cluster_centers_[:, 2],
        s=5,
        color="red",
    )

    ax.scatter(
        sample_pixels[sample_clusters == 0, 0],
        sample_pixels[sample_clusters == 0, 1],
        sample_pixels[sample_clusters == 0, 2],
        s=5,
        c="lightblue",
        marker="v",
        edgecolor="black",
        label="cluster 1",
    )
    ax.scatter(
        sample_pixels[sample_clusters == 1, 0],
        sample_pixels[sample_clusters == 1, 1],
        sample_pixels[sample_clusters == 1, 2],
        s=5,
        c="orange",
        marker="o",
        edgecolor="black",
        label="cluster 2",
    )
    ax.scatter(
        sample_pixels[sample_clusters == 2, 0],
        sample_pixels[sample_clusters == 2, 1],
        sample_pixels[sample_clusters == 2, 2],
        s=5,
        c="lightgreen",
        marker="s",
        edgecolor="black",
        label="cluster 3",
    )

    plt.show()
