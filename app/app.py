from dataclasses import replace
from email.mime import image
from multiprocessing.dummy import Array
from flask import Flask, render_template, url_for, request, redirect
import sys
from random import choice
from images import load_images_from_s3

import os


app = Flask(__name__)

LIKED = []
DISLIKED = []
MAYBE = []
# IMAGES = os.listdir(os.path.join(app.static_folder, "images"))
IMAGES = load_images_from_s3()


@app.route("/", methods=["GET", "POST"])
def base():
    """Root page that displats a naviagation bar,
    a local and its selection form, and liked selections

    Returns:
        Flask Response: the root page `/`
    """

    image_template = "static/images/{}"

    if not IMAGES:
        return render_template("caught_up.html")
    image = choice(IMAGES)

    # image1_obj = {"image_name": image, "image_path": image_template.format(image)}
    image1_obj = {"image_name": image, "image_path": image}

    if request.method == "POST":
        if "dislike" in request.form:
            img_name = request.form.get("image_name")
            DISLIKED.append(img_name)
            IMAGES.remove(img_name)
        if "maybe" in request.form:
            pass
        if "like" in request.form:
            img_name = request.form.get("image_name")
            LIKED.append(img_name)
            IMAGES.remove(img_name)

    print(f"Liked {LIKED}")
    print(f"DISLIKED {DISLIKED}")
    if not IMAGES:
        return render_template("caught_up.html")
    return render_template("base.html", image=image1_obj, rank=[])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
