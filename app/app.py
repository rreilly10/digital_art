from dataclasses import replace
from email.mime import image
from multiprocessing.dummy import Array
from flask import (
    Flask,
    render_template,
    send_from_directory,
    url_for,
    request,
    redirect,
)

from random import choice

from utils import like_local, dislike_local

import os

MEDIA_FOLDER = "/Users/robertreilly/code/digital_art/assets/images/out/large_comp/"

app = Flask(__name__)


IMAGES = os.listdir(MEDIA_FOLDER)


@app.route("/", methods=["GET"])
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

    image_obj = {"image_name": image, "image_path": image_template.format(image)}

    if not IMAGES:
        return render_template("caught_up.html")
    return render_template("base.html", image=image_obj, rank=[])


@app.route("/uploads/<path:filename>")
def download_file(filename):
    print(MEDIA_FOLDER, filename)
    return send_from_directory(MEDIA_FOLDER, filename, as_attachment=True)


@app.route("/like", methods=["POST"])
def like():
    if request.method == "POST":
        result = request.form
        print(result)

    return redirect("/")


@app.route("/dislike", methods=["POST"])
def dislike():
    if request.method == "POST":
        result = request.form
        if "dislike" in result:
            pass
        print(result)

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
