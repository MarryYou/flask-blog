from flask import Flask, Blueprint, render_template, url_for, redirect, request
from common.recommend import get_new_article

abouts = Blueprint("/abouts", __name__)


@abouts.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        recommend = get_new_article()
        return render_template("about.html", recommend=recommend)
